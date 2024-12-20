from typing import Literal

from custom_types import HitObject


def std_hit_objects_parser(
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

    # 初始化用于滑条持续时间解析的数据
    BASE_SLIDER_VELOCITY: float  # 基础滑条速度倍率
    timing_points_list: list[
        list[str]
    ]  # [TimingPoints] 下每行的数据，行内数据已被 .split(',')
    BASE_SLIDER_VELOCITY, timing_points_list = _init_slider_parser(osu_file_metadata)

    for hit_object in hit_objects_list:
        object_type: Literal["hit circle", "slider", "spinner", "hold", "unknown"] = (
            "unknown"
        )
        start_time: int | float = 0  # 毫秒
        end_time: int | float = 0

        object_params: list[str] = hit_object.split(",")

        # 处理下数据，十进制转二进制，然后去掉左边 0b 标识，补齐八位避免 IndexError，转换成字符串方便直接取位值
        raw_type: str = str(bin(int(object_params[3]))).removeprefix("0b").zfill(8)
        # 打击音效
        raw_hitSound: str = str(bin(int(object_params[4]))).removeprefix("0b").zfill(4)

        if raw_type[-1] == "1":
            # 音符（泡泡，米，Note）
            object_type = "hit circle"
            start_time = end_time = int(object_params[2])
        elif raw_type[-2] == "1":
            # 主模式滑条
            object_type = "slider"
            start_time = int(object_params[2])

            # 滑条持续时间计算
            slide_time: float = _slide_time_parser(
                BASE_SLIDER_VELOCITY=BASE_SLIDER_VELOCITY,
                timing_points_list=timing_points_list,
                object_params=object_params,
            )  # 要求是 int，实际计算这个会出现 float，输出 float 游戏也能读，那就这样了
            end_time = start_time + slide_time  # 这里计算得值是 float
        elif raw_type[-4] == "1":
            # 主模式转盘
            object_type = "spinner"
            start_time = int(object_params[2])
            end_time = int(object_params[5])
        elif raw_type[-8] == "1":
            # mania 长音符（长条，long note，LN，面）
            # 样例数据 448,192,31331,128,8,31836:2:0:0:0:
            object_type = "hold"
            start_time = int(object_params[2])
            end_time = int(object_params[5].split(":")[0])
        else:
            object_type = "unknown"

        rt_list.append(
            {"type": object_type, "start_time": start_time, "end_time": end_time}
        )

    return rt_list


def _init_slider_parser(osu_file_metadata: list[str]) -> tuple[float, list[list[str]]]:
    """初始化计算滑条持续时间所需的数据

    Args:
        osu_file_metadata (list[str]): .osu 文件元数据

    Returns:
        tuple[float, list[list[str]]]: (基础滑条速度倍率，[TimingPoints] 下每行的数据 (行内数据已被 .split(',')))
    """
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

    timing_points_list: list[list[str]] = []
    # 找出时间点，即 [TimingPoints] 下每行的数据，例如 320,337.078651685393,4,2,1,50,1,0 又例 32679,-100,4,2,1,60,0,0。已经去除行末换行符（\\n），用 , 分割为列表
    append_timing_points_list_flag: bool = False
    for line in osu_file_metadata:
        if append_timing_points_list_flag:
            if line.strip() == "":
                break

            timing_points_list.append(line.strip().split(","))
            continue

        if line.rstrip() == "[TimingPoints]":
            append_timing_points_list_flag = True

    # 倒转一下，这样在列表头的就是时间最后的
    timing_points_list.reverse()

    return (BASE_SLIDER_VELOCITY, timing_points_list)


def _slide_time_parser(
    BASE_SLIDER_VELOCITY: float,
    timing_points_list: list[list[str]],
    object_params: list[str],
) -> float:
    """滑条持续时间解析器

    Args:
        BASE_SLIDER_VELOCITY (float): 基础滑条速度倍率
        timing_points_list (list[list[str]]): [TimingPoints] 信息
        object_params (list[str]): 物件数据

    Returns:
        float: 滑条持续时间
    """
    start_time = int(object_params[2])
    # TODO: 此处 length 值应该是 Decimal 精确小数，滑条的视觉长度。单位是 osu! 像素。换高精库来算
    length = float(object_params[7])
    beat_length: float = -1.0

    # 找出当前 beat length，也就是找最接近的一根红线
    for timing_point in timing_points_list:
        if (
            int(timing_point[0]) <= start_time and timing_point[-2] == "1"
        ):  # 为非继承时间点（红线）
            # TODO: 换精确小数存储 beat_length
            beat_length = float(timing_point[1])
            break

    if beat_length == -1.0:
        # 如果还是 -1.0 说明压根没读到红线，非法数据
        ...

    # 找出当前 timing_point，计算 SV (slider_velocity_multiplier)
    slider_velocity_multiplier: int | float
    for timing_point in timing_points_list:
        if int(timing_point[0]) > start_time:
            continue

        if timing_point[-2] == "1":  # 为非继承时间点（红线）
            # 如果没有绿线控制，则 SV (slider_velocity_multiplier) 默认为 1
            slider_velocity_multiplier = 1
            break
        elif timing_point[-2] == "0":  # 为继承时间点（绿线）
            # TODO: 换精确小数计算 beat_length -> float(timing_point[1])
            slider_velocity_multiplier = 100 / -(float(timing_point[1]))
            break
        else:
            ...  # 非法数据

    # 计算滑条持续时间
    slide_time: float = (
        length / (BASE_SLIDER_VELOCITY * 100 * slider_velocity_multiplier) * beat_length
    )

    return slide_time
