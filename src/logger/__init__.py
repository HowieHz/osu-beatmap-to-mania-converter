import os
import pprint

from pywebio.output import put_error, put_info, put_warning

# 有文字都会转换成 true，所以不用担心报错
DEBUG_FLAG: bool = bool(os.getenv("DEBUG_FLAG"))

if DEBUG_FLAG:
    log_stream = open("debug.log", mode="a+", encoding="utf-8")


def debug(message: str, data: any = "", end: str | None = "\n") -> None:
    if DEBUG_FLAG:
        log_stream.write(f"[debug/开发分析]: {message}\n")
        log_stream.write(
            pprint.pformat(data, indent=4, width=160, sort_dicts=False) + "\n"
        )


def info(message: str) -> None:
    quiet_flag: bool = bool(os.getenv("QUIET_FLAG"))
    webui_flag: bool = bool(os.getenv("WEBUI_FLAG"))

    if quiet_flag:
        return

    if webui_flag:
        put_info(message)
        return

    print(f"[info/信息]: {message}")


def warning(message: str) -> None:
    webui_flag: bool = bool(os.getenv("WEBUI_FLAG"))
    if webui_flag:
        put_warning(message)
        return

    print(f"[warning/警告]: {message}")


def error(message: str) -> None:
    webui_flag: bool = bool(os.getenv("WEBUI_FLAG"))
    if webui_flag:
        put_error(message)
        return

    print(f"[error/错误]: {message}")
