from custom_types import ManiaHitObject


def mania_object_to_mania_1k(hit_object: ManiaHitObject) -> ManiaHitObject:
    """把物件添加到 mania 一轨

    Args:
        hit_object (ManiaHitObject): 转换前物件的信息

    Returns:
        ManiaHitObject: 转换后物件的信息
    """
    hit_object.update({"key": 1})

    return hit_object
