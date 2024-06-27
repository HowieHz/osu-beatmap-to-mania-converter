from typing import Literal, TypedDict

class NoTypeObject(TypedDict):
    """开始时间和结束时间单位是毫秒。\n
    """
    start_time: int | float
    end_time: int | float

class HitObject(NoTypeObject):
    """
    描述一个物件的信息\n

    type 取值在 "hit circle", "slider",  "spinner", "hold", "unknown" 中\n
    开始时间和结束时间单位是毫秒。\n
    要求结束是 int，实际计算滑条持续时间，会导致这个会出现 float。但是输出 float 游戏也能读，那就输出吧。
    """

    type: Literal["hit circle", "slider", "spinner", "hold", "unknown"]


class ManiaHitObject(NoTypeObject):
    """
    描述一个物件的信息\n

    type 取值在 "hit circle", "hold", "unknown" 中。\n
    开始时间和结束时间单位是毫秒。\n
    key 从左到右计数，最左边是 1。\n
    """
    type: Literal["hit circle", "hold", "unknown"]
    key: int


class ExternalManiaHitObject(NoTypeObject):
    """
    描述一个物件的信息\n

    type 取值在 "hit circle", "hold", "unknown", "end sign" 中。\n
    开始时间和结束时间单位是毫秒。\n
    key 从左到右计数，最左边是 1。\n
    """
    type: Literal["hit circle", "hold", "unknown", "end sign"]
    key: int


class Mania2kOptions(TypedDict):
    """_summary_

    Args:
        main_key (int): 惯用单戳键设置，1 为左，2 为右
        start_key (int): 铺面起手键，1 为左，2 为右
        trill_start_key (int): 交互起手键，1 为左，2 为右
        minimum_jack_time_interval (float): 最小叠键时间间距，单位毫秒。
        maximum_number_of_jack_notes (int): 最大叠键数。
    """

    main_key: Literal[1, 2]
    start_key: Literal[1, 2]
    trill_start_key: Literal[1, 2]
    minimum_jack_time_interval: float
    maximum_number_of_jack_notes: int
