from logger import debug, info, warning, error
from custom_types import HitObject, ManiaHitObject
from message import *

from reader import load_hit_objects_list, load_osu_file_metadata ,hit_objects_parser
from processor import std_object_type_to_mania, any_object_to_mania_1k, any_metadata_to_mania
from exporter import generate_mania_1k_osu_file, generate_mania_2k_osu_file


def main():
    print(PROGRAM_INFORMATION)
    print(PLEASE_PRESS_ENTER_AFTER_INPUT)
    
    # 获取 osu 文件路径
    osu_file_full_path: str = input(PLEASE_INPUT_YOUR_OSU_FILE_FULL_PATH)
    
    # 读取 osu 文件除去去 [HitObjects] 的信息
    osu_file_metadata: list[str] = load_osu_file_metadata(osu_file_full_path)
    debug("osu_file_metadata", data=osu_file_metadata)
    
    # 将 osu!std 元数据转换为 osu!mania 元数据
    osu_file_metadata = any_metadata_to_mania(osu_file_metadata)
    
    # 读取并解析 [HitObjects] 下每行的数据为更易于处理的形式
    parsed_hit_objects_list: list[HitObject] = hit_objects_parser(load_hit_objects_list(osu_file_full_path))
    
    # 滑条，转盘转 hold，并且给每条物件信息附加上在 mania 一轨的信息
    parsed_mania_1k_hit_objects_list: list[ManiaHitObject] = list(map(any_object_to_mania_1k, map(std_object_type_to_mania, parsed_hit_objects_list)))
    debug("parsed_mania_1k_hit_objects_list", data=parsed_mania_1k_hit_objects_list)
    
    number_of_keys: int = 0
    # 询问用户输出 mania 1k 还是 mania 2k
    while not number_of_keys in (1,2):
        number_of_keys = int(input(PLEASE_INPUT_THE_NUMBER_OF_KEYS_FOR_THE_CONVERTED_MANIA))
    
    # 目标产物 mania 1k
    if number_of_keys == 1:
        generate_mania_1k_osu_file(osu_file_metadata, parsed_mania_1k_hit_objects_list)
