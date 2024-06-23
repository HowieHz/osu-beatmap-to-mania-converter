from options_default import mania_2k_options_default, options_default

from ..cli_banner import CLI_BANNER
from ..const_url import *
from ..version import VERSION

# TODO: 制作中

# 共用介绍
DESCRIPTION: str = f"osu!std/osu!taiko(制作中) 转 osu!mania 铺面转换器 {VERSION}"

PROGRAM_INFORMATION: str = f"""\
{CLI_BANNER}

{DESCRIPTION}

{PROJECT_HOME_PAGE}: {PROJECT_HOME_PAGE_URL}
{DOWNLOAD_PAGE}: {DOWNLOAD_PAGE_URL}
{DOCUMENT_MIRROR_PAGE}: {DOCUMENT_MIRROR_PAGE_URL}
{ISSUE_FEEDBACK_PAGE}: {ISSUE_FEEDBACK_PAGE_URL}
"""
SHORT_PROGRAM_INFORMATION = f"""\
{CLI_BANNER}

{DESCRIPTION}"""

PLEASE_SUPPORT_THIS_PROJECT: str = (
    "如果您还感到满意，\n请到项目主页点个 star 吧支持本项目吧，\n您的支持将指引我砥砺前行！"
)

# webui 使用指导（最开头输出的信息）
PLEASE_PRESS_SUBMIT_BUTTON_AFTER_INPUT: str = "每条信息输入完成后，按下提交按钮。"

# webui 提示文字（一组输入框的标题）
BASIC_INFO: str = "基础信息"
STD_TO_MANIA_2k_4k: str = "osu!std 转 osu!mania 2k/4k 选项"

# webui 效验数据，返回的错误信息
THE_OPTION_CANNOT_BE_EMPTY: str = "此项不能为空"
THIS_IS_NOT_A_LEGAL_INPUT_VALUE: str = "这不是一个有效的输入值"

# cui 使用指导
PLEASE_PRESS_ENTER_AFTER_INPUT: str = "每条信息输入完成后，按下回车键。"
PLEASE_INPUT_YOUR_OSU_FILE_FULL_PATH: str = "输入被转换铺面的完整路径（.osu 结尾）"
PLEASE_INPUT_THE_NUMBER_OF_KEYS_FOR_THE_CONVERTED_MANIA: str = (
    f"输入转换后 Mania 铺面的键数 (如读取的是主模式铺面，输入 1, 2, 4 中的数值；如读取的是 Taiko 模式的铺面，输入 4, 5 中的数值，默认值为 {options_default['converter_output_number_of_keys']})。注：读取主模式铺面时，如设置输出键数为 4 ，即将 4k 左边两轨当 2k 使用。"
)
PLEASE_OUTPUT_DIR: str = (
    "指定输出的 .osu 文件的目录。输入为空则设定为 .osu 文件的同目录下"
)
PLEASE_OUTPUT_FILENAME: str = (
    "指定输出的 .osu 文件的文件名。输入为空则设定为 '原文件文件名(转换参数)'"
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
    f"输入铺面生成起始轨（1 为左，2 为右，默认值为 {mania_2k_options_default['start_key']}）"
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

# cli 运行输出
OUTPUT_DIR_IS: str = "输出目录为"
OUTPUT_FILENAME_IS: str = "输出文件名为"

LOADING_OSU_FILE: str = "读取文件中，请稍等..."
OSU_FILE_LOADED: str = "读取完成。"

CONVERTING_BEATMAP: str = "铺面文件转换中，请稍等..."
BEATMAP_CONVERTED: str = "铺面文件转换完成。"

WRITING_OSU_FILE: str = "铺面文件转换中，请稍等..."
OSU_FILE_WRITTEN: str = "铺面文件已完成写入。"

PROGRAM_HAS_BEEN_COMPLETED: str = "铺面已完成转换。"

RUNTIME_IS: str = "上一阶段运行花费了 {:.6f} 秒"

# cli 帮助文字

CLI_HELP_MESSAGE = "显示此帮助信息并退出程序"
CLI_HELP_QUIET = "使程序减少输出。--quiet 或 --quiet True 均可启用此选项"
CLI_HELP_CONFIG = f"配置文件路径。如仅添加 --config 不带参数，则为在 {options_default['config_file_path_root_and_stem']}.{options_default['config_file_type']} 创建配置文件并退出程序。如添加 --config yaml 则为初始化一个 yaml 格式的配置文件；--config json 则为初始化一个 json 格式的配置文件；--config toml 则为初始化一个 toml 格式的配置文件。注：json 和 toml 中路径出现的 \\ 字符要改成 \\\\，而 yaml 中字符串只能用单引号 ' 而不能用双引号 \" 标注。"
CLI_HELP_CONFIG_TYPE = "配置文件类型"
CLI_HELP_CUI = "进入交互式命令提示程序"
CLI_HELP_WEBUI = "进入 WebUI"
CLI_HELP_LOG_VERBOSITY = "修改输出详细程度"  # change output verbosity
CLI_HELP_VERSION = "输出软件版本信息并退出程序"

# cli 帮助文字前缀

CLI_STD_TO_MANIA_2K_PREFIX = "（适用于 std 转 mania 2k/4k 铺面的选项）"

# cli 程序报错设置

CLI_OSU_FILE_FULL_PATH_ARGUMENT_IS_REQUIRED = (
    "“被转换铺面的完整路径（.osu 结尾）”是必要的参数，请添加“-i 被转换铺面的完整路径”参数"
)
CLI_DONT_SUPPORT_OSU_CATCH_BEATMAP = "程序不支持 osu!catch 模式的铺面输入！"
CLI_DONT_SUPPORT_OSU_TAIKO_BEATMAP = "程序暂不支持 osu!taiko 模式的铺面输入！"
