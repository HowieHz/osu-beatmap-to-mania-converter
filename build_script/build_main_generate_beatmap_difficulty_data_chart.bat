pip install pyinstaller
del .\dist\obmc-beatmap-difficulty-data-chart-generator-latest.exe
pyinstaller .\src\main_generate_beatmap_difficulty_data_chart.py --onefile
ren .\dist\main_generate_beatmap_difficulty_data_chart.exe obmc-beatmap-difficulty-data-chart-generator-latest.exe
