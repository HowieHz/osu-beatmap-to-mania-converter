from custom_types import ManiaHitObject
from logger import debug, warning


def generate_mania_nk_osu_file(
    file_metadata: list[str], hit_objects_list: list[ManiaHitObject], keys: int
) -> str:
    """生成最终的 mania .osu 文件数据

    Args:
        file_metadata (list[str]): 铺面元数据
        hit_objects_list (list[ManiaHitObject]): 铺面物件数据
        keys (int): 铺面键数

    Returns:
        str: 文件数据，可直接写入 .osu 文件
    """
    debug("file_metadata", data=file_metadata)
    debug("hit_objects_list", data=hit_objects_list)

    # 生成元数据
    raw_file_metadata: str = "".join(file_metadata)

    # 生成 .osu 文件 [HitObjects] 这一段数据
    raw_hit_objects_list: str = "[HitObjects]\n"
    valid_value_list: list[int] = list(range(1, keys + 1))
    for hit_object in hit_objects_list:
        # 越界检测
        if hit_object["key"] not in valid_value_list:
            warning(f"{hit_object['key']} is not in list(range(1, {keys}+1))")

        x: int = _key_to_x(hit_object["key"], keys)

        if hit_object["type"] == "hit circle":
            # x,y,时间,物件类型,打击音效,物件参数,打击音效组（默认 0:0:0:0:）
            raw_hit_objects_list += f"{x},192,{hit_object['start_time']},1,0,0:0:0:0:\n"  # TODO 要能把打击音效和打击音效组继承过来
        elif hit_object["type"] == "hold":
            # x,y,开始时间,物件类型,长键音效,结束时间:长键音效组
            raw_hit_objects_list += f"{x},192,{hit_object['start_time']},128,0,{hit_object['end_time']}:0:0:0:0:\n"  # TODO 同上面
        else:
            pass

    # 文件末不用加空行，因为上面每行末尾都有\n，保持和制铺器生成的一致
    return raw_file_metadata + raw_hit_objects_list


def _key_to_x(key: int, keys: int) -> int:
    """key 位置转 x 值

    Args:
        key (int): key 位置，从左到右第一轨是 1
        keys (int): 多少 key 的铺面

    Returns:
        int: x 值
    """
    return int((key - 0.5) * 512 / keys)
