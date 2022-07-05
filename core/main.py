def main() -> None:
    from utils import out, misc, feedback, actions
    
    # clearing, printing banner and menu
    out.clear()
    out.banner()
    out.menu()

    # getting user action
    action = out.fancy_input("Action: ")
    action = int(action)
    if not misc.check_input_range(action, 1, 6):
        feedback.error("Action number does not exist.")

    # checking action
    actions.check_action(action)

    # resetting style
    out.reset_style()