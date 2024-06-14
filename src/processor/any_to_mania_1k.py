from custom_types import HitObject, ManiaHitObject

def any_to_mania_1k(hit_object: HitObject) -> ManiaHitObject:
    """把物件添加到 mania 一轨

    Args:
        hit_object (HitObject): 转换前物件的信息

    Returns:
        HitObject: 转换后物件的信息
    """
    hit_object.update({"key": 1})
    return hit_object
