from custom_types import HitObject
from logger import error

from ._mania_hit_objects_parser import mania_hit_objects_parser
from ._std_hit_objects_parser import std_hit_objects_parser
from ._taiko_hit_objects_parser import taiko_hit_objects_parser


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
    match _osu_file_metadata_mode_parser(osu_file_metadata):
        case "osu!":
            return std_hit_objects_parser(
                osu_file_metadata=osu_file_metadata, hit_objects_list=hit_objects_list
            )
        case "osu!taiko":
            return taiko_hit_objects_parser(
                osu_file_metadata=osu_file_metadata, hit_objects_list=hit_objects_list
            )
        case "osu!catch":
            error("程序不支持 osu!catch 模式的铺面输入！")
            ...
        case "osu!mania":
            return mania_hit_objects_parser(
                osu_file_metadata=osu_file_metadata, hit_objects_list=hit_objects_list
            )


def _osu_file_metadata_mode_parser(osu_file_metadata: list[str]) -> str:
    """解析 .osu 铺面的游戏模式

    Args:
        osu_file_metadata (list[str]): 铺面元数据

    Returns:
        str: 游戏模式，在 osu! osu!taiko osu!catch osu!mania 中取值， osu! 在制铺器里是选择 all
    """
    for line in osu_file_metadata:
        if line.startswith("Mode:"):
            mode: int = int(line.removeprefix("Mode:").strip())
            match mode:
                case 0:
                    return "osu!"
                case 1:
                    return "osu!taiko"
                case 2:
                    return "osu!catch"
                case 3:
                    return "osu!mania"
                case _:
                    return "osu!"
