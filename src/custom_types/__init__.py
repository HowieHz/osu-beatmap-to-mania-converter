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

    type 取值在 "hit circle", "slider",  "spinner", "hold", "unknown" 中。\n
    开始时间和结束时间单位是毫秒。\n
    key 从左到右计数，最左边是 1。\n
    """

    type: str
    start_time: int
    end_time: int
    key: int

class Mania2kOptions(TypedDict):
    start_key: int
    trill_start_key: int
