from multiprocessing import Process

import webview
from cli import cli_main
from pywebio import start_server
from pywebio.input import FLOAT, input
from pywebio.output import put_markdown, put_text

from logger import debug
from message import *
from reader import load_osu_file_metadata, osu_file_metadata_mode_parser


def webui():
    """webui main program"""
    put_text(PROGRAM_INFORMATION)
    put_text(PLEASE_PRESS_SUBMIT_BUTTON_AFTER_INPUT)
    put_markdown("---")

    while True:
        osu_file_full_path: str | None = None
        # 获取 osu 文件路径，去除两头的单双引号
        while osu_file_full_path in ("", None):
            osu_file_full_path: str = (
                input(PLEASE_INPUT_YOUR_OSU_FILE_FULL_PATH)
                .removeprefix('"')
                .removeprefix("'")
                .removesuffix('"')
                .removesuffix("'")
            )

        output_dir: str | None = None
        # 询问输出目录，去除两头的单双引号
        output_dir = (
            input(PLEASE_OUTPUT_DIR)
            .removeprefix('"')
            .removeprefix("'")
            .removesuffix('"')
            .removesuffix("'")
        )

        output_file_name: str | None = None
        # 询问输出文件名
        output_file_name = input(PLEASE_OUTPUT_FILENAME)

        number_of_keys: str | None = None
        # 询问用户输出 mania 1k 还是 mania 2k 还是 4k
        while number_of_keys not in ("1", "2", "4", "5", ""):
            number_of_keys = input(
                PLEASE_INPUT_THE_NUMBER_OF_KEYS_FOR_THE_CONVERTED_MANIA
            )

        # 询问是否移除变速
        remove_sv_option: str | None = None
        while remove_sv_option not in ("1", "2", "0", ""):
            remove_sv_option = input(PLEASE_INPUT_REMOVE_SV_OPTION)

        # std to mania 2k 生成参数询问部分
        std_to_mania_2k_main_key: str | None = None
        std_to_mania_2k_start_key: str | None = None  # 铺面起手键位置
        std_to_mania_2k_trill_start_key: str | None = None  # 交互起手键位置
        std_to_mania_2k_minimum_jack_time_interval: str | None = (
            None  # 最小叠键时间间距，单位毫秒
        )
        std_to_mania_2k_maximum_number_of_jack_notes: str | None = None  # 最大叠键数

        # 读取 osu 文件除去去 [HitObjects] 的信息
        osu_file_metadata: list[str] = load_osu_file_metadata(osu_file_full_path)
        debug("osu_file_game_mode", data=osu_file_metadata_mode_parser(osu_file_metadata))
        if osu_file_metadata_mode_parser(
            osu_file_metadata
        ) == "osu!" and number_of_keys in (
            "2",
            "4",
            "",  # 取默认值的、不输入的、直接回车的
        ):
            # 主要单戳纸询问
            while std_to_mania_2k_main_key not in ("1", "2", ""):
                std_to_mania_2k_main_key = input(MANIA_2k_PLEASE_INPUT_MAIN_KEY)

            # 起手键询问
            while std_to_mania_2k_start_key not in ("1", "2", ""):
                std_to_mania_2k_start_key = input(MANIA_2K_PLEASE_INPUT_START_KEY)

            # 交互起手键询问
            while std_to_mania_2k_start_key not in ("1", "2", ""):
                std_to_mania_2k_trill_start_key = input(
                    MANIA_2K_PLEASE_INPUT_TRILL_START_KEY
                )

            # 最小叠键时间间距询问
            std_to_mania_2k_minimum_jack_time_interval = input(
                MANIA_2K_PLEASE_INPUT_MINIMUM_JACK_TIME_INTERVAL
            )

            # 最大叠键数询问
            std_to_mania_2k_maximum_number_of_jack_notes = input(
                MANIA_2K_PLEASE_INPUT_MAXIMUM_NUMBER_OF_JACK_NOTES
            )

        # 构建命令行参数
        cli_arg_to_variable_dict: dict[str, str] = {
            "-i": osu_file_full_path,
            "-k": number_of_keys,
            "-o": output_dir,
            "-f": output_file_name,
            "-r": remove_sv_option,
            "-smk": std_to_mania_2k_main_key,
            "-ssk": std_to_mania_2k_start_key,
            "-stsk": std_to_mania_2k_trill_start_key,
            "-smjti": std_to_mania_2k_minimum_jack_time_interval,
            "-smnjn": std_to_mania_2k_maximum_number_of_jack_notes,
        }

        args_list: list[str] = []

        for arg in cli_arg_to_variable_dict.keys():
            if cli_arg_to_variable_dict[arg] not in ("", None):
                args_list.append(arg)
                args_list.append(cli_arg_to_variable_dict[arg])

        debug(message="args_list", data=args_list)
        # 发送到指令解析/实际逻辑运行
        cli_main(args_list)

        put_markdown("*" + PROGRAM_HAS_BEEN_COMPLETED + "*")
        put_text(PLEASE_SUPPORT_THIS_PROJECT)
        put_markdown("---")


def webui_process(port: int = 8099):
    PORT: int = port
    start_server(webui, port=PORT)


def window_process(port: int = 8099):
    PORT: int = port
    webview.create_window(
        f"osu-beatmap-to-mania-converter {VERSION}", f"http://127.0.0.1:{PORT}", width=1200, height=1000,
    )
    webview.start()


def webui_main(port: int = 8099):
    PORT: int = port

    webui_process_instance = Process(target=webui_process, args=(PORT,))
    window_process_instance = Process(target=window_process, args=(PORT,))

    webui_process_instance.start()
    window_process_instance.start()
    webui_process_instance.join()
    window_process_instance.join()


if __name__ == "__main__":
    webui_main()
