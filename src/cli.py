import argparse

from message import *

if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument("-v", "--version", action="store_true", help=CLI_HELP_VERSION)

    parser.add_argument(
        "-l",
        "--log-verbosity",
        help=CLI_HELP_LOG_VERBOSITY,
        type=str,
        choices=["info", "debug"],
        default="info",
    )
    parser.add_argument(
        "-i", "--osu_file_full_path", help=PLEASE_INPUT_YOUR_OSU_FILE_FULL_PATH
    )

    parser.add_argument(
        "-k",
        "--keys",
        help=PLEASE_INPUT_THE_NUMBER_OF_KEYS_FOR_THE_CONVERTED_MANIA,
        default=0,
        type=int,
        choices=[1, 2, 4, 5],
    )

    # 返回来自指定选项的某些数据
    args = parser.parse_args()

    if args.version:
        print(args.version)

    print(args.osu_file_full_path)

    if args.keys:
        print("keys turned on")
