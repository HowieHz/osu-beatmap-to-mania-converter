from custom_types import ManiaHitObject
from logger import debug, warning


def generate_mania_6k_osu_file(
    file_metadata: list[str], hit_objects_list: list[ManiaHitObject]
) -> str:
    debug("file_metadata", data=file_metadata)
    debug("hit_objects_list", data=hit_objects_list)

    # 生成元数据
    raw_file_metadata: str = "".join(file_metadata)

    # 生成 .osu 文件 [HitObjects] 这一段数据
    raw_hit_objects_list: str = "[HitObjects]\n"
    for hit_object in hit_objects_list:
        # 越界检测
        if hit_object["key"] not in (1, 2, 3, 4, 5, 6):
            warning(f"{hit_object['key']} is not in (1, 2, 3, 4, 5, 6)")

        match hit_object["key"]:
            case 1:
                x = 42
            case 2:
                x = 128
            case 3:
                x = 213
            case 4:
                x = 298
            case 5:
                x = 384
            case 6:
                x = 469
            case _:
                x = 469

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
