from typing import TypedDict


class OptionsDefaultDict(TypedDict):
    converter_output_number_of_keys: str
    remove_sv_mode: int
    config_file_full_path: str


options_default: OptionsDefaultDict = {
    "converter_output_number_of_keys": 4,
    "remove_sv_mode": 1,
    "config_file_full_path": "./config.toml",
}
