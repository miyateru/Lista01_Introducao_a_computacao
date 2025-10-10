class invalid_charset(Exception):
     pass

class invalid_syntax(Exception):
     pass

def check_charset(charset : dict[str : int], vector : str) -> None:
    for char in vector:
        if char not in charset.keys():
            raise invalid_charset(f"Character {char} is not in the valid charset (out of base)!")
    return None

def check_signal_placement(vector : str) -> None:
    if ('-' in vector) and (0 != vector.index('-')):
            raise invalid_syntax("Incorrect placement of signal!¡")
    return None
