from custom_types import ManiaHitObject
from logger import debug


def generate_mania_4k_osu_file(
    file_metadata: list[str], hit_objects_list: list[ManiaHitObject]
) -> str:
    debug("file_metadata", data=file_metadata)
    debug("hit_objects_list", data=hit_objects_list)

    # 生成元数据
    raw_file_metadata = "".join(file_metadata)

    # 米例：64,192,168,1,0,0:0:0:0:
    # 192,192,420,1,0,0:0:0:0:
    # 320,192,757,1,0,0:0:0:0:
    # 448,192,926,1,0,0:0:0:0:
    # 面例：64,192,1095,128,0,1347:0:0:0:0:
    # 192,192,1516,128,0,1853:0:0:0:0:
    # 320,192,2022,128,0,2443:0:0:0:0:
    # 448,192,2696,128,0,2948:0:0:0:0:

    # 生成 .osu 文件 [HitObjects] 这一段数据
    raw_hit_objects_list = "[HitObjects]\n"
    for hit_object in hit_objects_list:
        match hit_object["key"]:
            case 1:
                x = 64
            case 2:
                x = 192
            case 3:
                x = 320
            case 4:
                x = 448

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
