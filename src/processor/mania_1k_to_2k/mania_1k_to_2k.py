from custom_types import ManiaHitObject, Mania2kOptions


def mania_1k_to_2k(
    hit_objects_list: list[ManiaHitObject], options: Mania2kOptions | None = None
) -> list[ManiaHitObject]:
    if options == None:
        options: Mania2kOptions = {"start_key": 1, "trill_start_key": 1}

    # 设置铺面起手键
    hit_objects_list = _set_beatmap_start_key(options["start_key"] ,hit_objects_list)


def _set_beatmap_start_key(
    start_key: int, hit_objects_list: list[ManiaHitObject]
) -> list[ManiaHitObject]:
    """设置铺面起手键"""
    hit_objects_list[0]["key"] = start_key
    return hit_objects_list
