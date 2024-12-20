del .\dist\obmc-latest.exe
del .\dist\obmc-latest-noconsole.exe
del .\dist\obmc-beatmap-difficulty-data-chart-generator-latest.exe
pyinstaller .\src\main.py --onefile
ren .\dist\main.exe obmc-latest.exe
pyinstaller .\src\main.py --onefile --noconsole
ren .\dist\main.exe obmc-latest-noconsole.exe
pyinstaller .\src\main_generate_beatmap_difficulty_data_chart.py --onefile
ren .\dist\main_generate_beatmap_difficulty_data_chart.exe obmc-beatmap-difficulty-data-chart-generator-latest.exe
