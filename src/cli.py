import argparse
from pathlib import Path

from custom_types import HitObject, Mania2kOptions, ManiaHitObject
from exporter import (
    generate_mania_1k_osu_file,
    generate_mania_2k_osu_file,
    generate_mania_4k_osu_file,
    generate_mania_nk_osu_file,
)
from logger import error, info
from message import *
from options_default import mania_2k_options_default
from processor import (
    any_metadata_remove_sv,
    any_metadata_to_mania_1k,
    any_metadata_to_mania_2k,
    any_metadata_to_mania_4k,
    mania_1k_to_2k,
    std_object_type_to_mania_1k,
    taiko_object_type_to_mania_5k,
)
from reader import (
    hit_objects_parser,
    load_hit_objects_list,
    load_osu_file_metadata,
    osu_file_metadata_mode_parser,
)


def arg_parse() -> None:
    parser = argparse.ArgumentParser(description=DESCRIPTION)

    parser.add_argument(
        "-i", "--osu-file-full-path", help=PLEASE_INPUT_YOUR_OSU_FILE_FULL_PATH, type=str
    )

    parser.add_argument("-v", "--version", action="store_true", help=CLI_HELP_VERSION)

    # parser.add_argument(
    #     "-l",
    #     "--log-verbosity",
    #     help=CLI_HELP_LOG_VERBOSITY,
    #     type=str,
    #     choices=["info", "debug"],
    #     default="info",
    # )

    parser.add_argument(
        "-k",
        "--keys",
        help=PLEASE_INPUT_THE_NUMBER_OF_KEYS_FOR_THE_CONVERTED_MANIA,
        default=options_default["converter_output_number_of_keys"],
        type=int,
        choices=[1, 2, 4, 5],
    )

    parser.add_argument("-o", "--output-dir", help=PLEASE_OUTPUT_DIR, type=str)
    parser.add_argument("-f", "--output-file-name", help=PLEASE_OUTPUT_FILENAME, type=str)

    parser.add_argument(
        "-r",
        "--remove-sv-mode",
        help=PLEASE_INPUT_REMOVE_SV_OPTION,
        default=options_default["remove_sv_mode"],
        type=int,
        choices=[0, 1, 2],
    )

    parser.add_argument(
        "-smk",
        "--std-to-mania-2k-main-key",
        help=CLI_STD_TO_MANIA_2K_PREFIX + MANIA_2k_PLEASE_INPUT_MAIN_KEY,
        default=mania_2k_options_default["main_key"],
        type=int,
        choices=[1, 2],
    )

    parser.add_argument(
        "-ssk",
        "--std-to-mania-2k-start-key",
        help=CLI_STD_TO_MANIA_2K_PREFIX + MANIA_2K_PLEASE_INPUT_START_KEY,
        default=mania_2k_options_default["start_key"],
        type=int,
        choices=[1, 2],
    )

    parser.add_argument(
        "-stsk",
        "--std-to-mania-2k-trill-start-key",
        help=CLI_STD_TO_MANIA_2K_PREFIX + MANIA_2K_PLEASE_INPUT_TRILL_START_KEY,
        default=mania_2k_options_default["trill_start_key"],
        type=int,
        choices=[1, 2],
    )

    parser.add_argument(
        "-smjti",
        "--std-to-mania-2k-minimum-jack-time-interval",
        help=CLI_STD_TO_MANIA_2K_PREFIX
        + MANIA_2K_PLEASE_INPUT_MINIMUM_JACK_TIME_INTERVAL,
        default=mania_2k_options_default["minimum_jack_time_interval"],
        type=float,
    )

    parser.add_argument(
        "-smnjn",
        "--std-to-mania-2k-maximum-number-of-jack-notes",
        help=CLI_STD_TO_MANIA_2K_PREFIX
        + MANIA_2K_PLEASE_INPUT_MAXIMUM_NUMBER_OF_JACK_NOTES,
        default=mania_2k_options_default["maximum_number_of_jack_notes"],
        type=int,
    )

    # 返回来自指定选项的某些数据
    args = parser.parse_args()

    print(args)

    # 输出版本信息
    if args.version:
        print(PROGRAM_INFORMATION)
        return

    # 缺失必要参数
    if args.osu_file_full_path is None:
        print(CLI_OSU_FILE_FULL_PATH_ARGUMENT_IS_REQUIRED)
        return

    # 获取 osu 文件路径，去除两头的单双引号
    raw_osu_file_full_path: str = args.osu_file_full_path
    osu_file_full_path: str = (
        raw_osu_file_full_path.removeprefix('"')
        .removeprefix("'")
        .removesuffix('"')
        .removesuffix("'")
    )

    # 获取输出 mania keys 数
    raw_number_of_keys: int = args.keys
    number_of_keys: int = raw_number_of_keys

    # 获取输出目录，去除两头的单双引号
    raw_output_dir: str | None = args.output_dir
    output_dir: str = ""
    if raw_output_dir is None:
        output_dir = str(Path(osu_file_full_path).parent)
    else:
        output_dir = (
            raw_output_dir.removeprefix('"')
            .removeprefix("'")
            .removesuffix('"')
            .removesuffix("'")
        )
    if not output_dir.endswith(("\\", "/")):
        # 如果尾部没斜杠，就在末尾加斜杠。先检测前面是哪种斜杠，然后在尾部加一样的
        if "\\" in output_dir:
            output_dir += "\\"
        else:
            output_dir += "/"

    info(f"{OUTPUT_DIR_IS} {output_dir}")

    # 获取输出文件名
    raw_output_file_name: str | None = args.output_file_name
    output_file_name: str = ""
    if raw_output_file_name is None:
        output_file_name = str(
            Path(osu_file_full_path).stem
        )  # 注意这里是 stem 不是 name 所以是没有后缀的

    # 是否移除变速
    raw_remove_sv_option: int | None = args.remove_sv_mode
    remove_sv_option: str
    match raw_remove_sv_option:
        case 0:
            remove_sv_option = "none"
        case 1:
            remove_sv_option = "all"
        case 2:
            remove_sv_option = "inherited_timing_points"

    # 生成最后的文件名
    final_osu_file_name: str = (
        f"{output_file_name}({number_of_keys}k_remove_sv_{remove_sv_option}).osu"
    )
    info(f"{OUTPUT_FILENAME_IS} {final_osu_file_name}")

    # TODO: # std -> mania 2/4k 生成参数询问部分
    # 主要单戳指设置
    raw_std_to_mania_2k_main_key: int = args.std_to_mania_2k_main_key
    mania_2k_main_key: int = raw_std_to_mania_2k_main_key

    # 铺面起手键位置
    raw_std_to_mania_2k_start_key: int = args.std_to_mania_2k_start_key
    mania_2k_start_key: int = raw_std_to_mania_2k_start_key

    # 交互起手键位置
    raw_std_to_mania_2k_trill_start_key: int = args.std_to_mania_2k_trill_start_key
    mania_2k_trill_start_key: int = raw_std_to_mania_2k_trill_start_key

    # 最小叠键时间间距，单位毫秒
    raw_std_to_mania_2k_minimum_jack_time_interval: float = (
        args.std_to_mania_2k_minimum_jack_time_interval
    )
    mania_2k_minimum_jack_time_interval: float = (
        raw_std_to_mania_2k_minimum_jack_time_interval
    )

    # 最大叠键数
    raw_std_to_mania_2k_maximum_number_of_jack_notes: int = (
        args.std_to_mania_2k_maximum_number_of_jack_notes
    )
    mania_2k_maximum_number_of_jack_notes: int = (
        raw_std_to_mania_2k_maximum_number_of_jack_notes
    )

    # TODO 主逻辑部分
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

    match osu_file_metadata_mode_parser(osu_file_metadata):
        case "osu!":
            # 滑条，转盘转 hold，并且给每条物件信息附加上在 mania 一轨的信息
            parsed_mania_1k_hit_objects_list: list[ManiaHitObject] = list(
                map(std_object_type_to_mania_1k, parsed_hit_objects_list)
            )
        case "osu!taiko":
            parsed_mania_5k_hit_objects_list: list[ManiaHitObject] = list(
                map(taiko_object_type_to_mania_5k, parsed_hit_objects_list)
            )
        case "osu!catch":
            error(CLI_DONT_SUPPORT_OSU_CATCH_BEATMAP)
            return
        case "osu!mania":
            # TODO: mania 转 1k\2k
            ...

    info(OSU_FILE_LOADED)
    info(CONVERTING_BEATMAP)

    # 根据配置值去除 sv
    osu_file_metadata: list[str] = any_metadata_remove_sv(
        remove_sv_option=remove_sv_option, osu_file_metadata=osu_file_metadata
    )

    # 最后写入文件的内容
    final_osu_file_content: str

    match osu_file_metadata_mode_parser(osu_file_metadata):
        case "osu!":
            # 滑条，转盘转 hold，并且给每条物件信息附加上在 mania 一轨的信息
            parsed_mania_1k_hit_objects_list: list[ManiaHitObject] = list(
                map(std_object_type_to_mania_1k, parsed_hit_objects_list)
            )

            if number_of_keys == 1:
                # 目标产物 mania 1k
                # 将铺面元数据转换为 osu!mania 1k 元数据
                osu_file_metadata: list[str] = any_metadata_to_mania_1k(osu_file_metadata)

                ## 生成铺面
                final_osu_file_content = generate_mania_1k_osu_file(
                    osu_file_metadata, parsed_mania_1k_hit_objects_list
                )
            elif number_of_keys == 2 or number_of_keys == 4:
                # 目标产物 mania 2k

                # 将铺面从 1k 转换为 2k（根据配置项处理 parsed_mania_1k_hit_objects_list）
                parsed_mania_2k_hit_objects_list = mania_1k_to_2k(
                    parsed_mania_1k_hit_objects_list, options=mania_2k_options
                )

                ## 生成铺面
                if number_of_keys == 2:
                    # 将铺面元数据转换为 osu!mania 2k 元数据
                    osu_file_metadata: list[str] = any_metadata_to_mania_2k(
                        osu_file_metadata
                    )

                    final_osu_file_content = generate_mania_2k_osu_file(
                        osu_file_metadata, parsed_mania_2k_hit_objects_list
                    )
                elif number_of_keys == 4:
                    # 将铺面元数据转换为 osu!mania 4k 元数据
                    osu_file_metadata: list[str] = any_metadata_to_mania_4k(
                        osu_file_metadata
                    )

                    final_osu_file_content = generate_mania_4k_osu_file(
                        osu_file_metadata, parsed_mania_2k_hit_objects_list
                    )
        case "osu!taiko":
            parsed_mania_5k_hit_objects_list: list[ManiaHitObject] = list(
                map(taiko_object_type_to_mania_5k, parsed_hit_objects_list)
            )
        case "osu!catch":
            error(CLI_DONT_SUPPORT_OSU_CATCH_BEATMAP)
            return
        case "osu!mania":
            # TODO: mania 转 1k\2k
            ...

    info(BEATMAP_CONVERTED)
    info(WRITING_OSU_FILE)

    # 写入文件
    with open(f"{output_dir}{final_osu_file_name}", mode="w+", encoding="utf-8") as f:
        f.write(final_osu_file_content)

    info(OSU_FILE_WRITTEN)
    info(PLEASE_SUPPORT_THIS_PROJECT)
    info(PRESS_ENTER_EXIT_SOFTWARE)


if __name__ == "__main__":
    arg_parse()
