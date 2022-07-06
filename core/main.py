def main() -> None:
    from utils import out, misc, feedback, actions
    
    # checking if settings
    if not misc.check_settings():
        misc.create_settings()

    # clearing, printing banner and menu
    out.clear()
    out.banner()
    out.menu()

    # getting user action
    action = out.fancy_input("Action: ", True)
    try:
        action = int(action)
    except:
        feedback.error("Action not valid.")

    if not misc.check_input_range(action, 1, 6):
        feedback.error("Action number does not exist.")

    # checking action
    actions.check_action(action)

    # resetting style
    out.reset_style()