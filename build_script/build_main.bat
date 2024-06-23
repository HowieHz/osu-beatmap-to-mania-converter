del .\dist\obmc-latest.exe
del .\dist\obmc-latest-noconsole.exe
pyinstaller .\src\main.py --onefile
ren .\dist\main.exe obmc-latest.exe
pyinstaller .\src\main.py --onefile --noconsole
ren .\dist\main.exe obmc-latest-noconsole.exe
