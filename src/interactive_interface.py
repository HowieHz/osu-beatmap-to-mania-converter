import locale

import reader, processor, exporter, message
from logger import info, warning, error
from message import *


def main():
    print(PROGRAM_INFORMATION)
    print(PLEASE_PRESS_ENTER_AFTER_INPUT)
    osu_file_full_path: str = input(PLEASE_INPUT_YOUR_OSU_FILE_FULL_PATH)
    reader.hit_objects_parser(reader.load_osu_file(osu_file_full_path))