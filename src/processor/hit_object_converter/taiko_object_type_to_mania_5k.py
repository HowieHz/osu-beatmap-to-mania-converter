from custom_types import HitObject, ManiaHitObject

# TODO: 待完成


def taiko_object_type_to_mania_5k(hit_object: HitObject) -> ManiaHitObject:
    """将滑条，转盘转换为长条，其他的不用转换\n
    把物件添加到 mania 一轨

    Args:
        hit_object (HitObject): 转换前物件的信息

    Returns:
        ManiaHitObject: 转换后物件的信息
    """
    if hit_object["type"] in ("slider", "spinner"):
        hit_object["type"] = "hold"
    else:
        pass

    hit_object.update({"key": 1})

    return hit_object
