def check_input_range(text: str, min: int, max: int):
    if text >= min and text <= max:
        return True
    else:
        return False


def check_settings() -> bool:
    from os.path import exists
    from containers import consts
    return exists(consts.SETTINGS_PATH)


def create_settings() -> None:
    from utils import out
    from json import dumps
    from containers import consts

    out.clear()

    # getting server user and IP
    user = out.fancy_input("Enter the server's user: ")
    ip = out.fancy_input("Enter the server's IP: ")

    # converting to json
    json = {
        "user": user,
        "ip": ip
    }
    json = dumps(json)

    # saving to settings file
    with open(consts.SETTINGS_PATH, "w") as settings:
        settings.write(json)
        settings.close()