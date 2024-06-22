from cli import cli_main
from cui import cui_main

if __name__ == "__main__":
    ret: str = cli_main()
    if ret == "enter-cui":
        cui_main()
