import os, pprint

DEBUG_FLAG: bool = bool(
    os.getenv("DEBUG_FLAG")
)  # 有文字都会转换成 true，所以不用担心报错


def debug(message: str, data: any = "", debug_flag: bool = False, end: str | None = "\n") -> None:
    if DEBUG_FLAG or debug_flag:
        print(f"[debug/开发分析]: {message}", end=end)
        pprint.pprint(data, indent=4, width=160, sort_dicts=False)


def info(message: str) -> None:
    print(f"[info/信息]: {message}")


def warning(message: str) -> None:
    print(f"[warning/警告]: {message}")


def error(message: str) -> None:
    print(f"[error/错误]: {message}")
