from typing import Literal, cast

from custom_types import TaikoHitObject, ManiaHitObject


def taiko_object_type_to_mania_6k(
    hit_object: TaikoHitObject,
) -> ManiaHitObject:
    """将滑条，转盘转换为长条，其他的不用转换\n
    把物件添加到 mania 一轨

    Args:
        hit_object (TaikoHitObject): 转换前物件的信息

    Returns:
        ManiaHitObject: 转换后物件的信息
    """
    # 添加 Whistle（哨声）和 Clap（鼓掌）音效的圆圈会变为咔 kat（蓝色）音符，
    # 未添加这两种音效的圆圈则默认为咚 don（红色）音符。
    # 添加 Finish（镲）音效的物件会变为 large 大音符。
    # 滑条变为黄色连打 drum roll。
    # 转盘变为拨浪鼓音符 denden note。
    # 红大 红小 蓝大 蓝小 滑条 转盘 1-6

    note_type: Literal[
        "kat", "large kat", "don", "large don", "drum roll", "denden note", "unknown"
    ] = hit_object["type"]

    if note_type in ("kat", "large kat", "don", "large don"):
        hit_object["type"] = "hit circle"
    else:  # "drum roll", "denden note"
        hit_object["type"] = "hold"

    mania_hit_object = cast(ManiaHitObject, hit_object)
    match note_type:
        case "don":
            key_position = 2
        case "large don":
            key_position = 1
        case "kat":
            key_position = 4
        case "large kat":
            key_position = 3
        case "drum roll":
            key_position = 5
        case "denden note":
            key_position = 6
        case "unknown":
            key_position = 6

    mania_hit_object.update({"key": key_position})

    return mania_hit_object
