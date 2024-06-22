from pathlib import Path

from hpyculator import hpysettings


def get_settings_file_instance(
    settings_file_full_path: str,
) -> hpysettings.SettingsFileObject:
    path_instance: Path = Path(settings_file_full_path)
    return hpysettings.load(
        settings_dir_path=str(path_instance.parent),
        settings_file_name=str(path_instance.stem),
        settings_file_format=str(path_instance.suffix).removeprefix("."),
    )
