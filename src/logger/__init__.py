import os

DEBUG_FLAG: bool = bool(os.getenv('DEBUG_FLAG'))  # 有文字都会转换成 true，所以不用担心报错

def debug(message: str, debug_flag: bool = False) -> None:
    if DEBUG_FLAG or debug_flag: 
        print(f"[debug/开发分析]: {message}")

def info(message: str) -> None:
    print(f"[info/信息]: {message}")


def warning(message: str) -> None:
    print(f"[warning/警告]: {message}")


def error(message: str) -> None:
    print(f"[error/错误]: {message}")
