import locale

from logger import debug, info, warning, error
from custom_types import HitObject
from message import *

import reader, processor, exporter, message
from reader import load_hit_objects_list, load_osu_file_metadata ,hit_objects_parser
from processor.std_to_mania import std_object_type_to_mania, any_to_mania_1k


def main():
    print(PROGRAM_INFORMATION)
    print(PLEASE_PRESS_ENTER_AFTER_INPUT)
    
    # 获取 osu 文件路径
    osu_file_full_path: str = input(PLEASE_INPUT_YOUR_OSU_FILE_FULL_PATH)
    
    # 读取 osu 文件除去去 [HitObjects] 的信息
    osu_file_metadata: list[str] = load_osu_file_metadata(osu_file_full_path)
    debug("osu_file_metadata", data=osu_file_metadata)
    
    # 读取并解析 [HitObjects] 下每行的数据为更易于处理的形式
    parsed_hit_objects_list: list[HitObject] = hit_objects_parser(load_hit_objects_list(osu_file_full_path))
    
    # 滑条，转盘转 hold，并且给每条物件信息附加上在 mania 一轨的信息
    parsed_mania_hit_objects_list = map(any_to_mania_1k, map(std_object_type_to_mania, parsed_hit_objects_list))
    debug("parsed_mania_hit_objects_list", data=list(parsed_mania_hit_objects_list))