def check_action(action: int):
    from utils import feedback, out
    from core import main
    from os import name, system

    if action == 1:
        feedback.info("Retriving an SSH shell...")
        out.clear()
    
    elif action == 4:
        command = "nano settings.json"
        if name in ("nt", "dos"):
            command = "mousepad settings.json"
        system(command)
        main.main()

    elif action == 5:
        out.clear()
        feedback.info("This program was made by Marco Vidali.")
        feedback.info("Copyright ©  2022, Marco Vidali")
        main.main()

    elif action == 6:
        out.clear()
        exit(1)