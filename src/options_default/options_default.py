from typing import TypedDict


class OptionsDefaultDict(TypedDict):
    converter_output_number_of_keys: str
    remove_sv_mode: int
    config_path_dir: str
    config_file_name: str
    config_file_type: str
    config_file_full_path: str
    cli_quiet_option: str


options_default: OptionsDefaultDict = {
    "converter_output_number_of_keys": 4,
    "remove_sv_mode": 1,
    "config_path_dir": "./",
    "config_file_name": "config",
    "config_file_type": "json",
    "config_file_full_path": "./config.json",
    "cli_quiet_option": "False",
}
