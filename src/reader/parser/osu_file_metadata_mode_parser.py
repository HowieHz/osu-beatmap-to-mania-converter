def osu_file_metadata_mode_parser(osu_file_metadata: list[str]) -> str:
    """解析 .osu 铺面的游戏模式

    Args:
        osu_file_metadata (list[str]): 铺面元数据

    Returns:
        str: 游戏模式，在 osu! osu!taiko osu!catch osu!mania 中取值， osu! 在制铺器里是选择 all
    """
    for line in osu_file_metadata:
        if line.startswith("Mode:"):
            mode: int = int(line.removeprefix("Mode:").strip())
            match mode:
                case 0:
                    return "osu!"
                case 1:
                    return "osu!taiko"
                case 2:
                    return "osu!catch"
                case 3:
                    return "osu!mania"
                case _:
                    return "osu!"

    return "osu!"
