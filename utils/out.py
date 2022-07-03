def banner() -> None:
    from containers import consts
    print(consts.BANNER)


def menu() -> None:
    from os import get_terminal_size
    from containers import consts

    terminal_width = get_terminal_size()[0]
    space_between = int(terminal_width / 3)

    for item in consts.MENU_ITEMS:
        formatted_item = f"[{consts.MENU_ITEMS.index(item)}] {item}"
        formatted_item = formatted_item.center(space_between)
        print(formatted_item, end = "")

    print("\n")