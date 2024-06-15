from pathlib import Path

from logger import debug, info, warning, error
from custom_types import HitObject, ManiaHitObject, Mania2kOptions
from message import *

from options_default import mania_2k_options_default
from reader import load_hit_objects_list, load_osu_file_metadata, hit_objects_parser
from processor import (
    std_object_type_to_mania,
    any_object_to_mania_1k,
    any_metadata_to_mania_1k,
    any_metadata_to_mania_2k,
    any_metadata_to_mania_4k,
    any_metadata_remove_sv,
    mania_1k_to_2k,
)
from exporter import (
    generate_mania_1k_osu_file,
    generate_mania_2k_osu_file,
    generate_mania_4k_osu_file,
)


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
    raw_number_of_keys: str | None = None
    # 询问用户输出 mania 1k 还是 mania 2k 还是 4k
    while not raw_number_of_keys in ("1", "2", "4", ""):
        raw_number_of_keys = input(
            PLEASE_INPUT_THE_NUMBER_OF_KEYS_FOR_THE_CONVERTED_MANIA
        )
    if raw_number_of_keys == "":
        number_of_keys = 2
    else:
        number_of_keys = int(raw_number_of_keys)

    output_dir: str = ""
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

    output_filename: str = ""
    # 询问输出文件名
    output_filename = input(PLEASE_OUTPUT_FILENAME)
    if output_filename == "":
        output_filename = str(
            Path(osu_file_full_path).stem
        )  # 注意这里是 stem 不是 name 所以是没有后缀的

    # 生成最后的文件名
    final_osu_file_name: str = f"{output_filename}({number_of_keys}k).osu"
    info(f"{OUTPUT_FILENAME_IS}{final_osu_file_name}")

    # 询问是否移除变速
    remove_sv_option: str
    raw_remove_sv_option: str | None = None
    while not raw_remove_sv_option in ("1", "2", "0", ""):
        raw_remove_sv_option = input(PLEASE_INPUT_REMOVE_SV_OPTION)
    match raw_remove_sv_option:
        case "0":
            remove_sv_option = "none"
        case "1":
            remove_sv_option = "all"
        case "2":
            remove_sv_option = "inherited timing points"
        case _:
            remove_sv_option = "all"

    # mania 2k 生成参数询问部分
    mania_2k_main_key: int  # 主要单戳指设置
    mania_2k_start_key: int  # 铺面起手键位置
    mania_2k_trill_start_key: int  # 交互起手键位置
    mania_2k_minimum_jack_time_interval: float  # 最小叠键时间间距，单位毫秒
    mania_2k_maximum_number_of_jack_notes: int  # 最大叠键数

    if number_of_keys == 2 or number_of_keys == 4:
        # 主要单戳纸询问
        raw_mania_2k_main_key = input(MANIA_2k_PLEASE_INPUT_MAIN_KEY)
        if raw_mania_2k_main_key == "":
            mania_2k_main_key = mania_2k_options_default["main_key"]
        elif raw_mania_2k_main_key in ("1", "2"):
            mania_2k_main_key: int = int(raw_mania_2k_main_key)
        else:  # 输入值非法，取默认值
            mania_2k_main_key = mania_2k_options_default["main_key"]

        # 起手键询问
        raw_input_mania_2k_start_key = input(MANIA_2K_PLEASE_INPUT_START_KEY)
        if raw_input_mania_2k_start_key == "":
            mania_2k_start_key = mania_2k_options_default["start_key"]
        elif raw_input_mania_2k_start_key in ("1", "2"):
            mania_2k_start_key: int = int(raw_input_mania_2k_start_key)
        else:  # 输入值非法，取默认值
            mania_2k_start_key = mania_2k_options_default["start_key"]

        # 交互起手键询问
        raw_input_mania_2k_trill_start_key = input(
            MANIA_2K_PLEASE_INPUT_TRILL_START_KEY
        )
        if raw_input_mania_2k_trill_start_key == "":
            mania_2k_trill_start_key = mania_2k_start_key
        elif raw_input_mania_2k_trill_start_key in ("1", "2"):
            mania_2k_trill_start_key: int = int(raw_input_mania_2k_trill_start_key)
        else:  # 输入值非法，取默认值
            mania_2k_trill_start_key = mania_2k_options_default["trill_start_key"]

        # 最小叠键时间间距询问
        raw_input_mania_2k_minimum_jack_time_interval = input(
            MANIA_2K_PLEASE_INPUT_MINIMUM_JACK_TIME_INTERVAL
        )
        if raw_input_mania_2k_minimum_jack_time_interval == "":
            mania_2k_minimum_jack_time_interval = mania_2k_options_default[
                "minimum_jack_time_interval"
            ]
        else:
            mania_2k_minimum_jack_time_interval = float(
                raw_input_mania_2k_minimum_jack_time_interval
            )

        # 最大叠键数询问
        raw_input_maximum_number_of_jack_notes = input(
            MANIA_2K_PLEASE_INPUT_MAXIMUM_NUMBER_OF_JACK_NOTES
        )
        if raw_input_maximum_number_of_jack_notes == "":
            mania_2k_maximum_number_of_jack_notes = mania_2k_options_default[
                "maximum_number_of_jack_notes"
            ]
        else:
            mania_2k_maximum_number_of_jack_notes = int(
                raw_input_maximum_number_of_jack_notes
            )

        # 生成配置
        mania_2k_options: Mania2kOptions = {
            "main_key": mania_2k_main_key,
            "start_key": mania_2k_start_key,
            "trill_start_key": mania_2k_trill_start_key,
            "minimum_jack_time_interval": mania_2k_minimum_jack_time_interval,
            "maximum_number_of_jack_notes": mania_2k_maximum_number_of_jack_notes,
        }

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

    # 根据配置值去除 sv
    osu_file_metadata: list[str] = any_metadata_remove_sv(
        remove_sv_option=remove_sv_option, osu_file_metadata=osu_file_metadata
    )

    if number_of_keys == 1:
        # 目标产物 mania 1k
        # 将铺面元数据转换为 osu!mania 1k 元数据
        osu_file_metadata: list[str] = any_metadata_to_mania_1k(osu_file_metadata)

        ## 生成铺面
        final_osu_file_content: str = generate_mania_1k_osu_file(
            osu_file_metadata, parsed_mania_1k_hit_objects_list
        )
    elif number_of_keys == 2 or number_of_keys == 4:
        # 目标产物 mania 2k

        # 将铺面从 1k 转换为 2k
        parsed_mania_2k_hit_objects_list = mania_1k_to_2k(
            parsed_mania_1k_hit_objects_list, options=mania_2k_options
        )

        ## 生成铺面
        if number_of_keys == 2:
            # 将铺面元数据转换为 osu!mania 2k 元数据
            osu_file_metadata: list[str] = any_metadata_to_mania_2k(osu_file_metadata)

            final_osu_file_content: str = generate_mania_2k_osu_file(
                osu_file_metadata, parsed_mania_2k_hit_objects_list
            )
        elif number_of_keys == 4:
            # 将铺面元数据转换为 osu!mania 4k 元数据
            osu_file_metadata: list[str] = any_metadata_to_mania_4k(osu_file_metadata)

            final_osu_file_content: str = generate_mania_4k_osu_file(
                osu_file_metadata, parsed_mania_2k_hit_objects_list
            )

    info(BEATMAP_CONVERTED)
    info(WRITING_OSU_FILE)

    # 写入文件
    with open(f"{output_dir}{final_osu_file_name}", mode="w+", encoding="utf-8") as f:
        f.write(final_osu_file_content)

    info(OSU_FILE_WRITTEN)
    info(PLEASE_SUPPORT_THIS_PROJECT)
    input(PRESS_ENTER_EXIT_SOFTWARE)
