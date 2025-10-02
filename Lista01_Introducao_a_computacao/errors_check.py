def check_charset(charset : str, vector : str) -> None:
    for char in vector:
        if char not in charset:
            print(f"Character {char} is not in the valid charset (out of base)!")
            raise Exception
    return None

def check_signal_placement(vector : str) -> None:
    if ('-' in vector) and (0 != vector.index('-')):
            print("Incorrect placement of signal!¡")
            raise Exception
    return None
