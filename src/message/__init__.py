import locale

from .cli_banner import CLI_BANNER
from .const_url import (
    DOCUMENT_MIRROR_PAGE,
    DOCUMENT_MIRROR_PAGE_URL,
    DOWNLOAD_PAGE,
    DOWNLOAD_PAGE_URL,
    ISSUE_FEEDBACK_PAGE,
    ISSUE_FEEDBACK_PAGE_URL,
    PROJECT_HOME_PAGE,
    PROJECT_HOME_PAGE_URL,
)
from .version import VERSION

_lang: str|None = locale.getlocale()[0]

if _lang == "Chinese (Simplified)_China":
    from .i18n.chinese_simplified_china import *
else:  # default
    from .i18n.chinese_simplified_china import *

# TODO: rewrite by babel
