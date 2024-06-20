from typing import TypedDict


class OptionsDefaultDict(TypedDict):
    converter_output_number_of_keys: str


options_default: OptionsDefaultDict = {
    "converter_output_number_of_keys": 4,
}
