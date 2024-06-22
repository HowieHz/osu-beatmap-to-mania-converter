from typing import TypedDict


class OptionsDefaultDict(TypedDict):
    converter_output_number_of_keys: str
    remove_sv_mode: int
    config_file_path_root_and_stem: str
    config_file_type: str


options_default: OptionsDefaultDict = {
    "converter_output_number_of_keys": 4,
    "remove_sv_mode": 1,
    "config_file_path_root_and_stem": "./config",
    "config_file_type": "yaml",
}
