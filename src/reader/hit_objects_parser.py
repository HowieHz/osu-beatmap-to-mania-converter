import os

from logger import debug
from custom_types import HitObject

# hit_objects_list 现在每一项就是一个物件，对应数字解释
# 打击物件语法 x,  y,   时间, 物件类型, 打击音效, 物件参数, 打击音效组（默认 0:0:0:0:） （实际逗号后没空格）
# 例          64, 192, 2345, 1,       0,                 0:0:0:0: （实际逗号后没空格）因为是mania note，所以没物件参数
# 例          64, 192, 3116, 128,     0,                 3287:0:0:0:0:
# 滑条语法： x,y,开始时间,物件类型,打击音效,曲线类型|曲线点,滑动次数,长度,头尾音效,头尾音效组,打击音效组
# 转盘语法： x,y,开始时间,物件类型,转盘音效,结束时间,转盘音效组
# om长键语法： x,y,开始时间,物件类型,长键音效,结束时间,长键音效组
# mania y 有看见固定 0，也有看见固定 192，好像无所谓，4k x有 64 192 320 448

# 打击物件语法：x,y,时间,物件类型,打击音效,物件参数,打击音效组

# x（整型） 和 y（整型）： 物件的位置，原点在左上角，单位是 osu! 像素。
# 时间（整型）： 物件精确击打的时间。以谱面音频开始为原点，单位是毫秒。
# 物件类型（整型）： 一位标记物件类型的数据。参见：类型部分。
# 打击音效（整型）： 一位标记物件打击音效的数据。参见：音效部分。
# 物件参数（逗号分隔的数组）： 根据物件类型不同附加的一些参数。
# 打击音效组（冒号分隔的数组）： 击打物件时，决定具体该播放哪些音效的一些参数。与打击音效参数关系密切。参见：音效部分。如果没有设置特殊参数，则默认为 0:0:0:0:。

# 类型
# 物件类型参数是一个 8 位整数，每一位都有特殊的含义。
# 位次序	含义
# 0	将物件标记为圆圈 -1
# 1	将物件标记为滑条 -2
# 2	标记新 Combo 起始物件 -3
# 3	将物件标记为转盘 -4
# 4, 5, 6	一个 3 位整数，指定要跳过多少 Combo 颜色（即“跳过连击色 (Colour hax)”）。仅在物件位于新 Combo 开始时才相关。 -5 -6 -7
# 7	将物件标记为 osu!mania 长按音符 -8
# 0 位是最低位


def hit_objects_parser(
    osu_file_metadata: list[str], hit_objects_list: list[str]
) -> list[HitObject]:
    """解析 [HitObjects] 下每行的数据为更易于处理的形式

    Args:
        osu_file_metadata (list[str]): 铺面元数据
        hit_objects_list (list[str]): [HitObjects] 下每行的数据，例如 256,192,11000,21,2

    Returns:
        list[HitObject]: 一个列表，装了解析后的铺面描述
    """
    rt_list: list[HitObject] = []

    # 找出 基础滑条速度倍率：Base slider velocity in hundreds of osu! pixels per beat
    BASE_SLIDER_VELOCITY: float = 0.0
    for line in osu_file_metadata:
        if line.startswith("SliderMultiplier:"):
            # TODO: 此处值应该是 Decimal 精确小数，换高精库来算
            BASE_SLIDER_VELOCITY = float(
                osu_file_metadata[osu_file_metadata.index(line)]
                .removeprefix("SliderMultiplier:")
                .strip()
            )
            break

    timing_points_list: list[str] = []
    # 找出时间点，即 [TimingPoints] 下每行的数据，例如 320,337.078651685393,4,2,1,50,1,0 又例 32679,-100,4,2,1,60,0,0。已经去除行末换行符（\\n）
    append_timing_points_list_flag: bool = False
    for line in osu_file_metadata:
        if append_timing_points_list_flag:
            if line.strip() == "":
                break

            timing_points_list.append(line.strip())
            continue
        
        if line.rstrip() == "[TimingPoints]":
            append_timing_points_list_flag = True
    
    print(timing_points_list)

    for hit_object in hit_objects_list:
        type: str = ""
        start_time: int = 0  # 毫秒
        end_time: int = 0

        object_params: list[str] = hit_object.split(",")
        debug("object_params", data=object_params)
        raw_type: str = (
            str(bin(int(object_params[3]))).removeprefix("0b").zfill(8)
        )  # 处理下数据，十进制转二进制，然后去掉左边 0b 标识，补齐八位避免 IndexError，转换成字符串方便直接取位值
        debug("raw_type", data=raw_type)

        if raw_type[-1] == "1":
            type = "hit circle"
            start_time = end_time = int(object_params[2])
            debug("hit circle time", data=start_time)
        elif raw_type[-2] == "1":
            type = "slider"
            start_time = int(object_params[2])
            debug("slider start time", data=start_time)

            # TODO: 此处 length 值应该是 Decimal 精确小数，滑条的视觉长度。单位是 osu! 像素。换高精库来算
            length = float(object_params[-4])

            given_by_effective_inherited_timing_point: bool = (
                False  # 如果这个滑条受继承时间点（绿线）控制，则为 True
            )
            # 如果没有绿线控制，则 SV (slider_velocity_multiplier) 默认为 1
            slider_velocity_multiplier = (
                1 if not given_by_effective_inherited_timing_point else 0
            )

            # 计算滑条持续时间
            # slide_time = length / (BASE_SLIDER_VELOCITY * 100 * slider_velocity_multiplier) * beatLength
            slide_time = 1000

            end_time = start_time + slide_time
            debug("spinner end time", data=end_time)
        elif raw_type[-4] == "1":
            type = "spinner"
            start_time = int(object_params[2])
            end_time = int(object_params[5])
            debug("spinner start time", data=start_time)
            debug("spinner end time", data=end_time)
        elif raw_type[-8] == "1":
            type = "hold"
            start_time = int(object_params[2])
            end_time = int(object_params[5])
            debug("hold start time", data=start_time)
            debug("hold end time", data=end_time)
        else:
            type = "unknown"

        rt_list.append({"type": type, "start_time": start_time, "end_time": end_time})

    debug("rt_list", data=rt_list)
    return rt_list
