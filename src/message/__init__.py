import locale

from .cli_banner import CLI_BANNER
from .version import VERSION

_lang: str = locale.getlocale()[0]

if _lang == "Chinese (Simplified)_China":
    from .i18n.chinese_simplified_china import *
else:  # default
    from .i18n.chinese_simplified_china import *

# TODO: rewrite by babel
