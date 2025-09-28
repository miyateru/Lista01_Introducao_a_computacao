def hex_to_dec(b: str) -> int:
    decimal : int = 0
    negativo : bool = False

    equivalencia : dict[str, int] = {
        "0" : 0,
        "1" : 1,
        "2" : 2,
        "3" : 3,
        "4" : 4,
        "5" : 5,
        "6" : 6,
        "7" : 7,
        "8" : 8,
        "9" : 9,
        "A" : 10,
        "B" : 11,
        "C" : 12,
        "D" : 13,
        "E" : 14,
        "F" : 15,
    }

    b = b.upper()

    if ("-" in b) and (0 != b.index("-")):
        raise ValueError
    
    for N in range(len(b)):
        if (b[N] not in equivalencia) and (b[N] != "-"):
            raise TypeError

    if "-" in b:
        negativo = True
        b = b.replace("-", "")

    b = b[::-1]
    
    for N in range(len(b)):
        decimal += equivalencia[b[N]] * (16 ** N)

    if negativo:
        decimal *= (-1)

    return decimal

def main () -> None:
    num = input(" > ")
    
    print(hex_to_dec(num))

    return None

if __name__ == "__main__":
    main()