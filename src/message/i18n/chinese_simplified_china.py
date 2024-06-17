from ..version import VERSION

PROGRAM_INFORMATION: str = f"""\
osu!std 转 osu!mania 铺面转换器
版本: {VERSION}

项目主页: https://github.com/HowieHz/osu-beatmap-to-mania-converter
下载地址: https://github.com/HowieHz/osu-beatmap-to-mania-converter/releases
我的博客: https://howiehz.top
问题反馈: https://github.com/HowieHz/osu-beatmap-to-mania-converter/issues/new/choose
"""
PLEASE_PRESS_ENTER_AFTER_INPUT: str = "每条信息输入完成后，请按下回车键。"
PLEASE_INPUT_YOUR_OSU_FILE_FULL_PATH: str = "请输入你的铺面完整路径（.osu 结尾）："
PLEASE_INPUT_THE_NUMBER_OF_KEYS_FOR_THE_CONVERTED_MANIA: str = (
    "请输入转换后 Mania 铺面的键数（请输入 1，2，4 中的数值，默认值为 2）\n注：设置输出渐键数为 4，即将 4k 左边两轨当 2k 使用。这样玩家无需制作 2k 界面所用皮肤。："
)
PLEASE_OUTPUT_DIR: str = (
    "请指定输出的 .osu 文件的目录。直接回车则为选择的 .osu 文件的同目录下："
)
PLEASE_OUTPUT_FILENAME: str = (
    "请指定输出的 .osu 文件的文件名。直接回车则为 '原文件文件名(转换参数)'："
)
OUTPUT_DIR_IS: str = "输出目录为："
OUTPUT_FILENAME_IS: str = "输出文件名为："

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
    "请输入是否移除铺面变速（0 为不移除，1 为全移除，2 为仅移除继承时间点（绿线），默认值为 1）"
)

# mania 2k only
# MANIA_2K_PLEASE_INPUT_

MANIA_2k_PLEASE_INPUT_MAIN_KEY: str = (
    "请输入惯用单戳指所在的轨道，物件将优先生成在这个轨道上（1 为左，2 为右，默认值为 1）"
)
MANIA_2K_PLEASE_INPUT_START_KEY: str = (
    "请输入铺面生成起始轨（1 为左，2 为右，默认值为 1）："
)
MANIA_2K_PLEASE_INPUT_TRILL_START_KEY: str = (
    "请输入交互起始轨（1 为左，2 为右，默认值为取铺面生成起始轨的值）："
)
MANIA_2K_PLEASE_INPUT_MINIMUM_JACK_TIME_INTERVAL: str = (
    "请输入最小叠键时间间距，两键间距小于这个值的才有可能被转换为切。可为整数或小数，单位毫秒（默认值为 200.0）："
)
MANIA_2K_PLEASE_INPUT_MAXIMUM_NUMBER_OF_JACK_NOTES: str = (
    "请输入最大叠键数，请输入一个整数（默认值为 1）"
)
