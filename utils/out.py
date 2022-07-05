def red() -> None:
    from colorama import Fore
    print(Fore.RED)
def white() -> None:
    from colorama import Fore
    print(Fore.WHITE)

def normal() -> None:
    from colorama import Style
    print(Style.NORMAL)
def bright() -> None:
    from colorama import Style
    print(Style.BRIGHT)
def reset_style() -> None:
    from colorama import Style
    print(Style.RESET_ALL)


def clear() -> None:
    from os import name, system
    command = "clear"
    if name in ("nt", "dos"):
        command = "cls"
    system(command)


def banner() -> None:
    from os import get_terminal_size
    from containers import consts

    terminal_width = get_terminal_size()[0]
    
    formatted_banner = ""
    for line in consts.BANNER.split("\n"):
        line = line.center(terminal_width)
        formatted_banner += f"{line}\n"

    red()
    bright()
    print(formatted_banner)


def menu() -> None:
    from os import get_terminal_size
    from containers import consts

    terminal_width = get_terminal_size()[0]
    space_between = int(terminal_width / 3)

    white()
    normal()
    for item in consts.MENU_ITEMS:
        formatted_item = f"[{consts.MENU_ITEMS.index(item) + 1}] {item}"
        formatted_item = formatted_item.center(space_between)
        print(formatted_item, end = "")

    print("\n")


def fancy_input(prompt: str) -> str:
    from os import get_terminal_size
    print("\n")

    space = (round(get_terminal_size()[0] / 2)) - len(prompt) - 1
    prompt = f"{' ' * space}{prompt}"

    result = input(prompt)

    return result