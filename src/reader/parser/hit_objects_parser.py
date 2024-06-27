from custom_types import HitObject, ManiaHitObject
from logger import error
from message import (
    CLI_DONT_SUPPORT_OSU_CATCH_BEATMAP,
    CLI_DONT_SUPPORT_UNEXPECTED_MOD_BEATMAP,
)

from ._mania_hit_objects_parser import mania_hit_objects_parser
from ._std_hit_objects_parser import std_hit_objects_parser
from ._taiko_hit_objects_parser import taiko_hit_objects_parser
from .osu_file_metadata_mode_parser import osu_file_metadata_mode_parser


def hit_objects_parser(
    osu_file_metadata: list[str], hit_objects_list: list[str]
) -> list[ManiaHitObject] | list[HitObject] | None:
    """解析 [HitObjects] 下每行的数据为更易于处理的形式

    Args:
        osu_file_metadata (list[str]): 铺面元数据
        hit_objects_list (list[str] | None): [HitObjects] 下每行的数据，例如 256,192,11000,21,2。

    Returns:
        list[ManiaHitObject] | list[HitObject] | None: 一个列表，装了解析后的铺面描述，返回 None 代表程序停止。
    """
    match osu_file_metadata_mode_parser(osu_file_metadata):
        case "osu!":
            return std_hit_objects_parser(
                osu_file_metadata=osu_file_metadata, hit_objects_list=hit_objects_list
            )
        case "osu!taiko":
            return taiko_hit_objects_parser(
                osu_file_metadata=osu_file_metadata, hit_objects_list=hit_objects_list
            )
        case "osu!catch":
            error(CLI_DONT_SUPPORT_OSU_CATCH_BEATMAP)
            return None
        case "osu!mania":
            return mania_hit_objects_parser(
                osu_file_metadata=osu_file_metadata, hit_objects_list=hit_objects_list
            )
        case _:
            error(CLI_DONT_SUPPORT_UNEXPECTED_MOD_BEATMAP)
            return None
