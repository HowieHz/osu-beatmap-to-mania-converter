from typing import TypedDict, Union


class HitObject(TypedDict):
    """
    描述一个物件的信息\n

    type 取值在 "hit circle", "slider",  "spinner", "hold", "unknown" 中\n
    开始时间和结束时间单位是毫秒。\n
    """

    type: str
    start_time: int
    end_time: int


class ManiaHitObject(HitObject):
    """
    描述一个物件的信息\n

    type 取值在 "hit circle", "slider",  "spinner", "hold", "unknown", "end sign" 中。\n
    开始时间和结束时间单位是毫秒。\n
    key 从左到右计数，最左边是 1。\n
    """

    type: str
    start_time: int
    end_time: int
    key: int

class Mania2kOptions(TypedDict):
    """_summary_

    Args:
        start_key (int): 铺面起手键，1 为左，2 为右
        trill_start_key (int): 交互起手键，1 为左，2 为右
        maximum_jack_time_interval (float): 最大叠键时间间距，单位毫秒。
        maximum_number_of_jack_notes (int): 最大叠键数。
    """
    start_key: int
    trill_start_key: int
    maximum_jack_time_interval: float
    maximum_number_of_jack_notes: int
