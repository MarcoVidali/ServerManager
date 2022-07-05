def error(text: str) -> None:
    from os import get_terminal_size
    from time import sleep
    from core import main
    from utils import out
    from containers import consts

    terminal_width = get_terminal_size()[0]

    print("\n")
    out.red()

    text = f"[-] {text}"
    text = text.center(terminal_width)
    print(text)

    out.reset_style()
    sleep(consts.FEEDBACK_SLEEP_TIME)

    main.main()

def info(text: str) -> None:
    from os import get_terminal_size
    from time import sleep
    from utils import out
    from containers import consts

    terminal_width = get_terminal_size()[0]

    print("\n")
    out.blue()

    text = f"[*] {text}"
    text = text.center(terminal_width)
    print(text)

    out.reset_style()
    sleep(consts.FEEDBACK_SLEEP_TIME)