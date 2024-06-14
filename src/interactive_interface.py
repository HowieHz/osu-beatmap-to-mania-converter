from pathlib import Path

from logger import debug, info, warning, error
from custom_types import HitObject, ManiaHitObject
from message import *

from reader import load_hit_objects_list, load_osu_file_metadata, hit_objects_parser
from processor import (
    std_object_type_to_mania,
    any_object_to_mania_1k,
    any_metadata_to_mania_1k,
    any_metadata_to_mania_2k,
)
from exporter import generate_mania_1k_osu_file, generate_mania_2k_osu_file


def main():
    print(PROGRAM_INFORMATION)
    print(PLEASE_PRESS_ENTER_AFTER_INPUT)

    osu_file_full_path: str = ""
    # 获取 osu 文件路径，去除两头的单双引号
    while osu_file_full_path == "":
        osu_file_full_path: str = (
            input(PLEASE_INPUT_YOUR_OSU_FILE_FULL_PATH)
            .removeprefix('"')
            .removeprefix("'")
            .removesuffix('"')
            .removesuffix("'")
        )

    number_of_keys: int = 0
    # 询问用户输出 mania 1k 还是 mania 2k
    while not number_of_keys in (1, 2):
        number_of_keys = int(
            input(PLEASE_INPUT_THE_NUMBER_OF_KEYS_FOR_THE_CONVERTED_MANIA)
        )

    output_dir = ""
    # 询问输出目录，去除两头的单双引号
    output_dir = (
        input(PLEASE_OUTPUT_DIR)
        .removeprefix('"')
        .removeprefix("'")
        .removesuffix('"')
        .removesuffix("'")
    )
    if output_dir == "":
        output_dir = str(Path(osu_file_full_path).parent)

    if not output_dir.endswith(("\\", "/")):
        # 如果尾部没斜杠，就在末尾加斜杠。先检测前面是哪种斜杠，然后在尾部加一样的
        if "\\" in output_dir:
            output_dir += "\\"
        else:
            output_dir += "/"

    info(f"{OUTPUT_DIR_IS}{output_dir}")

    output_filename = ""
    # 询问输出文件名
    output_filename = input(PLEASE_OUTPUT_FILENAME)
    if output_filename == "":
        output_filename = str(
            Path(osu_file_full_path).stem
        )  # 注意这里是 stem 不是 name 所以是没有后缀的

    # 生成最后的文件名
    final_osu_file_name = f"{output_filename}({number_of_keys}k).osu"
    info(f"{OUTPUT_FILENAME_IS}{final_osu_file_name}")

    info(LOADING_OSU_FILE)

    # 读取 osu 文件除去去 [HitObjects] 的信息
    osu_file_metadata: list[str] = load_osu_file_metadata(osu_file_full_path)

    # 读取并解析 [HitObjects] 下每行的数据为更易于处理的形式
    parsed_hit_objects_list: list[HitObject] = hit_objects_parser(
        osu_file_metadata, load_hit_objects_list(osu_file_full_path)
    )

    # 滑条，转盘转 hold，并且给每条物件信息附加上在 mania 一轨的信息
    parsed_mania_1k_hit_objects_list: list[ManiaHitObject] = list(
        map(
            any_object_to_mania_1k,
            map(std_object_type_to_mania, parsed_hit_objects_list),
        )
    )

    info(OSU_FILE_LOADED)
    info(CONVERTING_BEATMAP)

    if number_of_keys == 1:
        # 目标产物 mania 1k
        # 将铺面元数据转换为 osu!mania 1k 元数据
        osu_file_metadata = any_metadata_to_mania_1k(osu_file_metadata)

        ## 生成铺面
        final_osu_file_content: str = generate_mania_1k_osu_file(
            osu_file_metadata, parsed_mania_1k_hit_objects_list
        )
    elif number_of_keys == 2:
        # 目标产物 mania 2k
        # 将铺面元数据转换为 osu!mania 2k 元数据
        osu_file_metadata = any_metadata_to_mania_2k(osu_file_metadata)

        # TODO: 上面要询问一些参数，然后这里进行处理

        ## 生成铺面
        final_osu_file_content: str = generate_mania_2k_osu_file(
            osu_file_metadata, parsed_mania_1k_hit_objects_list
        )

    info(BEATMAP_CONVERTED)
    info(WRITING_OSU_FILE)

    # 写入文件
    with open(f"{output_dir}{final_osu_file_name}", mode="w+", encoding="utf-8") as f:
        f.write(final_osu_file_content)

    info(OSU_FILE_WRITTEN)
    info(PLEASE_SUPPORT_THIS_PROJECT)
    input(PRESS_ENTER_EXIT_SOFTWARE)
