def main() -> None:
    from utils import out
    
    # clearing, printing banner and menu
    out.clear()
    out.banner()
    out.menu()

    # getting user action
    out.fancy_input("Action: ")

    # resetting style
    out.reset_style()