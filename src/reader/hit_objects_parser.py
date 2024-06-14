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

# 类型
# 物件类型参数是一个 8 位整数，每一位都有特殊的含义。
# 位次序	含义
# 0	将物件标记为圆圈
# 1	将物件标记为滑条
# 2	标记新 Combo 起始物件
# 3	将物件标记为转盘
# 4, 5, 6	一个 3 位整数，指定要跳过多少 Combo 颜色（即“跳过连击色 (Colour hax)”）。仅在物件位于新 Combo 开始时才相关。
# 7	将物件标记为 osu!mania 长按音符

def hit_objects_parser(hit_objects_list: list[str]) -> list[HitObject]:
    """解析 [HitObjects] 下每行的数据为更易于处理的形式

    Args:
        hit_objects_list (list[str]): [HitObjects] 下每行的数据，例如 256,192,11000,21,2

    Returns:
        list[HitObject]: 一个列表，装了解析后的铺面描述
    """
    for hit_object in hit_objects_list:
        object_params: list[str] = hit_object.split(",")
        debug(f"object_params: {object_params}")
        debug(bin(object_params[3]))