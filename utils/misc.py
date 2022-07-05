def check_input_range(text: str, min: int, max: int):
    if text >= min and text <= max:
        return True
    else:
        return False