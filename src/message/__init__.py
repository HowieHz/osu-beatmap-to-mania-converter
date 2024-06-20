import locale

from .version import VERSION

_lang: str = locale.getlocale()[0]

CLI_LOGO = "   ____  ____  __  _________\n  / __ \\/ __ )/  |/  / ____/\n / / / / __  / /|_/ / /     \n/ /_/ / /_/ / /  / / /___   \n\\____/_____/_/  /_/\\____/   \n                            \n"

if _lang == "Chinese (Simplified)_China":
    from .i18n.chinese_simplified_china import *
else:  # default
    from .i18n.chinese_simplified_china import *
