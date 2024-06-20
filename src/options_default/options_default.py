from typing import TypedDict


class OptionsDefaultDict(TypedDict):
    converter_output_number_of_keys: str
    remove_sv_mode: int


options_default: OptionsDefaultDict = {
    "converter_output_number_of_keys": 4,
    "remove_sv_mode": 1,
}
