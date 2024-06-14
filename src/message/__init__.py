import locale

from .version import VERSION

_lang: str = locale.getdefaultlocale()[0]

PROGRAM_INFORMATION: str = f"""\
osu!std 转 osu!mania 铺面转换器
版本: {VERSION}

开源地址: https://github.com/HowieHz/osu-standard-to-mania-converter
下载地址: https://github.com/HowieHz/osu-standard-to-mania-converter/releases
我的博客: https://howiehz.top
问题反馈: https://github.com/HowieHz/osu-standard-to-mania-converter/issues/new/choose
"""
PLEASE_PRESS_ENTER_AFTER_INPUT: str = "每条信息输入完成后，请按下回车键。"
PLEASE_INPUT_YOUR_OSU_FILE_FULL_PATH: str = "请输入你的铺面完整路径（.osu 结尾）："
