from typing import TypedDict

from custom_types import ManiaHitObject, Mania2kOptions
from logger import debug
from options_default import mania_2k_options_default


class IndexManiaHitObject(TypedDict):
    """...

    Args:
        index (int): 此项物件数据在 hit_objects_list 中的索引
        hit_object (ManiaHitObject): 此项物件数据
    """

    index: int
    hit_object: ManiaHitObject


def mania_1k_to_2k(
    hit_objects_list: list[ManiaHitObject], options: Mania2kOptions | None = None
) -> list[ManiaHitObject]:
    if options == None:
        options: Mania2kOptions = mania_2k_options_default

    # 设置铺面起手键
    hit_objects_list = _set_beatmap_start_key(
        start_key=options["start_key"], hit_objects_list=hit_objects_list
    )

    # 长纵连转交互
    hit_objects_list = _convert_long_jack_to_trill(
        trill_start_key=options["trill_start_key"],
        maximum_jack_time_interval=options["maximum_jack_time_interval"],
        maximum_number_of_jack_notes=options["maximum_number_of_jack_notes"],
        hit_objects_list=hit_objects_list,
    )

    return hit_objects_list


def _set_beatmap_start_key(
    hit_objects_list: list[ManiaHitObject], start_key: int
) -> list[ManiaHitObject]:
    """设置铺面起手键"""
    hit_objects_list[0]["key"] = start_key
    return hit_objects_list


def _convert_long_jack_to_trill(
    trill_start_key: int,
    maximum_jack_time_interval: float,
    maximum_number_of_jack_notes: int,
    hit_objects_list: list[ManiaHitObject],
) -> list[ManiaHitObject]:
    """将铺面的长叠转换成交互"""

    # 这个列表包括了全部检测出来的长 jack，每项是包括一串长 jack 信息的列表
    long_jack_node_stack_list: list[list[IndexManiaHitObject]] = []

    # 创建一个栈（列表），每项是个 IndexManiaHitObject
    jack_node_stack: list[IndexManiaHitObject] = []

    jack_flag = False  # 这个为 False 表示现在并没有已经创建的 jack 栈

    # TODO: 创建配置选项 要求两叠键距离恒定才能转换
    jack_interval: int  # 用于存储两叠键之间的间隔

    # 把长 jack 筛选出来
    last_hit_object: ManiaHitObject = hit_objects_list[0]
    for index, hit_object in enumerate(
        hit_objects_list[1:] + [{"type": "end sign"}], start=1
    ):
        this_hit_object: ManiaHitObject = hit_object

        if this_hit_object["type"] == "end sign":  # 读取到尾部了
            if jack_flag and len(jack_node_stack) > maximum_number_of_jack_notes:
                long_jack_node_stack_list.append(jack_node_stack)
                jack_node_stack = []  # 无意义的清空
            break

        # 是否符合 jack 要求
        if (
            this_hit_object["start_time"] - last_hit_object["start_time"]
        ) < maximum_jack_time_interval:
            if index - 1 == 0:
                jack_node_stack.append({"index": 0, "hit_object": last_hit_object})
            jack_node_stack.append({"index": index, "hit_object": this_hit_object})
            jack_flag = True
        else:
            if jack_flag:  # 说明 jack 停止了
                # 检查是否满足长 jack 要求
                if len(jack_node_stack) > maximum_number_of_jack_notes:
                    long_jack_node_stack_list.append(jack_node_stack)
                jack_node_stack = []
                jack_flag = False

        last_hit_object = this_hit_object

    # 开始处理长叠键为切
    for jack_node_stack in long_jack_node_stack_list:
        hit_objects_list[jack_node_stack[0]["index"]]["key"] = trill_start_key

        for stack_index, this_index_hit_object in enumerate(
            jack_node_stack[1:], start=1
        ):
            last_index_hit_object = jack_node_stack[stack_index - 1]
            debug(last_index_hit_object)
            debug(hit_objects_list[last_index_hit_object["index"]] == last_index_hit_object["hit_object"])

            debug("last:",hit_objects_list[last_index_hit_object["index"]]["key"])
            debug("this:",hit_objects_list[this_index_hit_object["index"]]["key"])
            
            if hit_objects_list[last_index_hit_object["index"]]["key"] == 1:
                hit_objects_list[this_index_hit_object["index"]]["key"] = 2
            else:
                hit_objects_list[this_index_hit_object["index"]]["key"] = 1

    return hit_objects_list
