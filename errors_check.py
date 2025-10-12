class invalid_charset(Exception):
     pass

class invalid_syntax(Exception):
     pass

def charset(charset : dict[str, int | None], vector : str) -> None:
    for char in vector:
        if char not in charset.keys():
            raise invalid_charset
    return None

def signal_placement(vector : str) -> None:
    if ('-' in vector) and (0 != vector.index('-')):
            raise invalid_syntax
    return None
