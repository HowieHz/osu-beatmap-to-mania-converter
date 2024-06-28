import webbrowser
from multiprocessing import Process
from typing import Literal, TypedDict

import webview
from pywebio import start_server
from pywebio.input import input, input_group
from pywebio.output import put_buttons, put_code, put_markdown, put_text, put_warning

from cli import cli_main
from logger import debug
from message import *
from reader import load_osu_file_metadata, osu_file_metadata_mode_parser


class BasicDataDict(TypedDict):
    osu_file_full_path: str
    output_dir: str
    output_file_name: str
    number_of_keys: Literal["1", "2", "4", "5", ""]
    remove_sv_option: Literal["0", "1", "2", ""]


class StdToMania2kOptionsDataDict(TypedDict):
    std_to_mania_2k_main_key: Literal["1", "2", ""]
    std_to_mania_2k_start_key: Literal["1", "2", ""]
    std_to_mania_2k_trill_start_key: Literal["1", "2", ""]
    std_to_mania_2k_minimum_jack_time_interval: str
    std_to_mania_2k_maximum_number_of_jack_notes: str


def _check_osu_file_full_path(osu_file_full_path: str) -> str | None:
    if osu_file_full_path == "":  # 如果为空，此处值为 ""
        return THE_OPTION_CANNOT_BE_EMPTY
    return None


def _check_number_of_keys(number_of_keys: str) -> str | None:
    if number_of_keys not in ("1", "2", "4", "5", ""):
        return THIS_IS_NOT_A_LEGAL_INPUT_VALUE
    return None


def _check_remove_sv_option(remove_sv_option: str) -> str | None:
    if remove_sv_option not in ("0", "1", "2", ""):
        return THIS_IS_NOT_A_LEGAL_INPUT_VALUE
    return None


def _check_std_to_mania_2k_main_key(std_to_mania_2k_main_key: str) -> str | None:
    if std_to_mania_2k_main_key not in ("1", "2", ""):
        return THIS_IS_NOT_A_LEGAL_INPUT_VALUE
    return None


def _check_std_to_mania_2k_start_key(std_to_mania_2k_start_key: str) -> str | None:
    if std_to_mania_2k_start_key not in ("1", "2", ""):
        return THIS_IS_NOT_A_LEGAL_INPUT_VALUE
    return None


def _check_std_to_mania_2k_trill_start_key(
    std_to_mania_2k_trill_start_key: str,
) -> str | None:
    if std_to_mania_2k_trill_start_key not in ("1", "2", ""):
        return THIS_IS_NOT_A_LEGAL_INPUT_VALUE
    return None


def webui():
    """webui main program\n
    输入引导 webui\n
    输入值效验 webui\\cli\n
    参数列构建 webui\n
    """

    def open_page(choice: str) -> None:
        target_url: str
        if choice == PROJECT_HOME_PAGE:
            target_url = PROJECT_HOME_PAGE_URL
        elif choice == DOWNLOAD_PAGE:
            target_url = DOWNLOAD_PAGE_URL
        elif choice == DOCUMENT_MIRROR_PAGE:
            target_url = DOCUMENT_MIRROR_PAGE_URL
        elif choice == ISSUE_FEEDBACK_PAGE:
            target_url = ISSUE_FEEDBACK_PAGE_URL
        elif choice == ENTER_QQ_GROUP:
            target_url = QQ_GROUP_LINK
        webbrowser.open(target_url)

    put_code(SHORT_PROGRAM_INFORMATION)
    put_buttons(
        [
            PROJECT_HOME_PAGE,
            DOWNLOAD_PAGE,
            DOCUMENT_MIRROR_PAGE,
            ISSUE_FEEDBACK_PAGE,
            ENTER_QQ_GROUP,
        ],
        onclick=open_page,
    )
    put_text(PLEASE_PRESS_SUBMIT_BUTTON_AFTER_INPUT)
    put_markdown("---")

    while True:
        basic_data: BasicDataDict = input_group(
            BASIC_INFO,
            [
                input(
                    PLEASE_INPUT_YOUR_OSU_FILE_FULL_PATH,
                    name="osu_file_full_path",
                    validate=_check_osu_file_full_path,
                ),
                input(PLEASE_OUTPUT_DIR, name="output_dir"),
                input(PLEASE_OUTPUT_FILENAME, name="output_file_name"),
                input(
                    PLEASE_INPUT_THE_NUMBER_OF_KEYS_FOR_THE_CONVERTED_MANIA,
                    name="number_of_keys",
                    validate=_check_number_of_keys,
                    help_text=PLEASE_INPUT_THE_NUMBER_OF_KEYS_FOR_THE_CONVERTED_MANIA_HELP_TEXT,
                ),
                input(
                    PLEASE_INPUT_REMOVE_SV_OPTION,
                    name="remove_sv_option",
                    validate=_check_remove_sv_option,
                ),
            ],
        )

        # 获取 osu 文件路径，去除两头的单双引号
        osu_file_full_path: str = (
            basic_data["osu_file_full_path"]
            .removeprefix('"')
            .removeprefix("'")
            .removesuffix('"')
            .removesuffix("'")
        )
        # 获取输出目录，去除两头的单双引号
        output_dir: str = (
            basic_data["output_dir"]
            .removeprefix('"')
            .removeprefix("'")
            .removesuffix('"')
            .removesuffix("'")
        )
        # 获取输出文件名
        output_file_name: str = basic_data["output_file_name"]
        # 询问用户输出 mania ?k
        number_of_keys: Literal["1", "2", "4", "5", ""] = basic_data["number_of_keys"]
        # 询问是否移除变速
        remove_sv_option: Literal["0", "1", "2", ""] = basic_data["remove_sv_option"]

        # std to mania 2k 生成参数询问部分
        std_to_mania_2k_main_key: Literal["1", "2", ""] = ""
        std_to_mania_2k_start_key: Literal["1", "2", ""] = ""  # 铺面起手键位置
        std_to_mania_2k_trill_start_key: Literal["1", "2", ""] = ""  # 交互起手键位置
        std_to_mania_2k_minimum_jack_time_interval: str = ""  # 最小叠键时间间距，单位毫秒
        std_to_mania_2k_maximum_number_of_jack_notes: str = ""  # 最大叠键数

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
            std_to_mania_2k_options_data: StdToMania2kOptionsDataDict = input_group(
                STD_TO_MANIA_2k_4k,
                [
                    input(
                        MANIA_2k_PLEASE_INPUT_MAIN_KEY,
                        name="std_to_mania_2k_main_key",
                        validate=_check_std_to_mania_2k_main_key,
                    ),
                    input(
                        MANIA_2K_PLEASE_INPUT_START_KEY,
                        name="std_to_mania_2k_start_key",
                        validate=_check_std_to_mania_2k_start_key,
                    ),
                    input(
                        MANIA_2K_PLEASE_INPUT_TRILL_START_KEY,
                        name="std_to_mania_2k_trill_start_key",
                        validate=_check_std_to_mania_2k_trill_start_key,
                    ),
                    input(
                        MANIA_2K_PLEASE_INPUT_MINIMUM_JACK_TIME_INTERVAL,
                        name="std_to_mania_2k_minimum_jack_time_interval",
                    ),
                    input(
                        MANIA_2K_PLEASE_INPUT_MAXIMUM_NUMBER_OF_JACK_NOTES,
                        name="std_to_mania_2k_maximum_number_of_jack_notes",
                    ),
                ],
            )

            # 主要单戳纸询问
            std_to_mania_2k_main_key = std_to_mania_2k_options_data[
                "std_to_mania_2k_main_key"
            ]
            # 起手键询问
            std_to_mania_2k_start_key = std_to_mania_2k_options_data[
                "std_to_mania_2k_start_key"
            ]
            # 交互起手键询问
            std_to_mania_2k_trill_start_key = std_to_mania_2k_options_data[
                "std_to_mania_2k_trill_start_key"
            ]
            # 最小叠键时间间距询问，单位毫秒
            std_to_mania_2k_minimum_jack_time_interval = std_to_mania_2k_options_data[
                "std_to_mania_2k_minimum_jack_time_interval"
            ]
            # 最大叠键数询问
            std_to_mania_2k_maximum_number_of_jack_notes = std_to_mania_2k_options_data[
                "std_to_mania_2k_maximum_number_of_jack_notes"
            ]

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

        put_warning(PLEASE_SUPPORT_THIS_PROJECT)
        put_markdown("---")


def webui_process(port: int):
    PORT: int = port
    start_server(webui, port=PORT)


def window_process(port: int):
    PORT: int = port
    webview.create_window(
        f"osu-beatmap-to-mania-converter {VERSION}",
        f"http://127.0.0.1:{PORT}",
        width=1200,
        height=1000,
    )
    webview.start()


def webui_main(port: int):
    PORT: int = port

    webui_process_instance = Process(target=webui_process, args=(PORT,))
    window_process_instance = Process(target=window_process, args=(PORT,))

    webui_process_instance.start()
    window_process_instance.start()
    webui_process_instance.join()
    window_process_instance.join()


if __name__ == "__main__":
    webui_main(28099)
