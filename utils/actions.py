def check_action(action: int):
    from utils import feedback, out
    from core import main
    from containers import consts
    from os import name, system
    from json import load
    from os.path import exists

    if action == 1:
        feedback.info("Retriving an SSH shell...")
        
        # opening settings.json
        with open(consts.SETTINGS_PATH, "r") as json:
            content = load(json)
            user = content["user"]
            ip = content["ip"]

        # connecting with SSH
        out.clear()

        system(f"ssh {user}@{ip}")

        main.main()
    
    elif action == 2:
        out.clear()

        # opening settings.json
        with open(consts.SETTINGS_PATH, "r") as json:
            content = load(json)
            user = content["user"]
            ip = content["ip"]

        file_or_dir = out.fancy_input("File or directory (file-dir)? ")
        file_or_dir == file_or_dir.lower()

        if file_or_dir == "file":
            path = out.fancy_input("Enter the file path: ")

            if exists(path):
                destination = out.fancy_input("Enter the destination: ")
                out.clear()
                system(f"scp {path} {user}@{ip}:{destination}")
            else:
                feedback.error("File doesn't exist.")

        elif file_or_dir == "dir":
            path = out.fancy_input("Enter the dir path: ")

            if exists(path):
                destination = out.fancy_input("Enter the destination: ")
                out.clear()
                system(f"scp -r {path} {user}@{ip}:{destination}")
            else:
                feedback.error("Directory doesn't exist.")

        else:
            feedback.error("Choice not valid (file-dir)!")

        main.main()

    elif action == 3:
        out.clear()
        
        # opening settings.json
        with open(consts.SETTINGS_PATH, "r") as json:
            content = load(json)
            user = content["user"]
            ip = content["ip"]

        system(f"ssh {user}@{ip} 'sudo apt update -y && sudo apt upgrade -y'")

        main.main()


    elif action == 4:
        from containers import consts
        
        command = f"nano {consts.SETTINGS_PATH}"
        if name in ("nt", "dos"):
            command = f"notepad {consts.SETTINGS_PATH}"
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