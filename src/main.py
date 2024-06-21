from cli import arg_parse
from cui import cui_main

if __name__ == "__main__":
    ret: None | str = arg_parse()
    if ret == "enter-cui" or ret != "stop":
        cui_main()
