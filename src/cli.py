import argparse
from pathlib import Path

from logger import info
from message import *


def arg_parse() -> None:
    parser = argparse.ArgumentParser(description=DESCRIPTION)

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
        "osu_file_full_path", help=PLEASE_INPUT_YOUR_OSU_FILE_FULL_PATH, type=str
    )

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

    # 返回来自指定选项的某些数据
    args = parser.parse_args()

    print(args)

    if args.version:
        print(PROGRAM_INFORMATION)
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

    # 生成最后的文件名
    final_osu_file_name: str = f"{output_file_name}({number_of_keys}k).osu"
    info(f"{OUTPUT_FILENAME_IS} {final_osu_file_name}")

    # 是否移除变速
    raw_remove_sv_option: int | None = args.remove_sv_mode
    remove_sv_option: str
    match raw_remove_sv_option:
        case 0:
            remove_sv_option = "none"
        case 1:
            remove_sv_option = "all"
        case 2:
            remove_sv_option = "inherited timing points"

    # TODO: # mania 2k 生成参数询问部分
    mania_2k_main_key: int  # 主要单戳指设置
    mania_2k_start_key: int  # 铺面起手键位置
    mania_2k_trill_start_key: int  # 交互起手键位置
    mania_2k_minimum_jack_time_interval: float  # 最小叠键时间间距，单位毫秒
    mania_2k_maximum_number_of_jack_notes: int  # 最大叠键数

    # TODO 主逻辑部分


if __name__ == "__main__":
    arg_parse()
