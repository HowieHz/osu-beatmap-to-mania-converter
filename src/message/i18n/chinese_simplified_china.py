from options_default import mania_2k_options_default, options_default

from ..cli_logo import CLI_LOGO
from ..version import VERSION

DESCRIPTION: str = f"osu!std/osu!taiko 转 osu!mania 铺面转换器 {VERSION}"

PROGRAM_INFORMATION: str = f"""\
{CLI_LOGO}
{DESCRIPTION}

项目主页: https://github.com/HowieHz/osu-beatmap-to-mania-converter
下载地址: https://github.com/HowieHz/osu-beatmap-to-mania-converter/releases
文档镜像: https://howiehz.top/archives/osu-beatmap-to-mania-converter-readme
问题反馈: https://github.com/HowieHz/osu-beatmap-to-mania-converter/issues/new/choose
"""
PLEASE_PRESS_ENTER_AFTER_INPUT: str = "每条信息输入完成后，按下回车键。"
PLEASE_INPUT_YOUR_OSU_FILE_FULL_PATH: str = "输入被转换铺面的完整路径（.osu 结尾）"
PLEASE_INPUT_THE_NUMBER_OF_KEYS_FOR_THE_CONVERTED_MANIA: str = (
    f"输入转换后 Mania 铺面的键数 (如读取的是主模式铺面，输入 1, 2, 4 中的数值；如读取的是 Taiko 模式的铺面，输入 4, 5 中的数值，默认值为 {options_default['converter_output_number_of_keys']})。注：读取主模式铺面时，如设置输出键数为 4 ，即将 4k 左边两轨当 2k 使用。"
)
PLEASE_OUTPUT_DIR: str = (
    "指定输出的 .osu 文件的目录。直接回车则为选择的 .osu 文件的同目录下"
)
PLEASE_OUTPUT_FILENAME: str = (
    "指定输出的 .osu 文件的文件名。直接回车则为 '原文件文件名(转换参数)'"
)
OUTPUT_DIR_IS: str = "输出目录为"
OUTPUT_FILENAME_IS: str = "输出文件名为"

LOADING_OSU_FILE: str = "读取文件中，请稍等..."
OSU_FILE_LOADED: str = "读取完成。"

CONVERTING_BEATMAP: str = "铺面文件转换中，请稍等..."
BEATMAP_CONVERTED: str = "铺面文件转换完成。"

WRITING_OSU_FILE: str = "铺面文件转换中，请稍等..."
OSU_FILE_WRITTEN: str = "铺面文件已完成写入。"

PLEASE_SUPPORT_THIS_PROJECT: str = (
    "如果您还感到满意，\n请到项目主页点个 star 吧支持本项目吧，\n您的支持将指引我砥砺前行！"
)

PRESS_ENTER_EXIT_SOFTWARE: str = "按回车退出本程序。"

PLEASE_INPUT_REMOVE_SV_OPTION: str = (
    f"输入是否移除铺面变速（0 为不移除，1 为全移除，2 为仅移除继承时间点（绿线），默认值为 {options_default['remove_sv_mode']}）"
)

# mania 2k only
# MANIA_2K_PLEASE_INPUT_

MANIA_2k_PLEASE_INPUT_MAIN_KEY: str = (
    f"输入惯用单戳指所在的轨道，物件将优先生成在这个轨道上（1 为左，2 为右，默认值为 {mania_2k_options_default['main_key']}）"
)
MANIA_2K_PLEASE_INPUT_START_KEY: str = (
    f"输入铺面生成起始轨（1 为左，2 为右，默认值为 {mania_2k_options_default["start_key"]}）"
)
MANIA_2K_PLEASE_INPUT_TRILL_START_KEY: str = (
    f"输入交互起始轨（1 为左，2 为右，默认值为 {mania_2k_options_default['trill_start_key']}）"
)
MANIA_2K_PLEASE_INPUT_MINIMUM_JACK_TIME_INTERVAL: str = (
    f"输入最小叠键时间间距，两键间距小于这个值的才有可能被转换为切。可为整数或小数，单位毫秒（默认值为 {mania_2k_options_default['minimum_jack_time_interval']}）"
)
MANIA_2K_PLEASE_INPUT_MAXIMUM_NUMBER_OF_JACK_NOTES: str = (
    f"输入最大叠键数，值类型为整数（默认值为 {mania_2k_options_default['maximum_number_of_jack_notes']}）"
)

# cli help

CLI_HELP_MESSAGE = "显示此帮助信息并退出程序"
CLI_HELP_LOG_VERBOSITY = "修改输出详细程度"  # change output verbosity
CLI_HELP_VERSION = "输出软件版本信息"

# cli help prefix

CLI_STD_TO_MANIA_2K_PREFIX = "（适用于 std 转 mania 2k/4k 铺面的选项）"

# cli error

CLI_OSU_FILE_FULL_PATH_ARGUMENT_IS_REQUIRED = (
    "“被转换铺面的完整路径（.osu 结尾）”是必要的参数，请添加“-i 被转换铺面的完整路径”参数"
)
