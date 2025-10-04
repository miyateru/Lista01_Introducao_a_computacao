import errors_check

def hex_to_dec(b: str) -> int:
    char_table : dict[str, int] = {
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
    decimal : int = 0
    negative : bool = False

    b = b.upper()

    errors_check.check_signal_placement(b)
    
    for N in range(len(b)):
        if (b[N] not in char_table) and (b[N] != "-"):
            raise TypeError

    if "-" in b:
        negative = True
        b = b.replace("-", "")

    b = b[::-1]
    
    for N in range(len(b)):
        decimal += char_table[b[N]] * (16 ** N)

    if negative:
        decimal *= (-1)

    return decimal

def main () -> None:
    num = input(" > ")
    print(hex_to_dec(num))

    return None

if __name__ == "__main__":
    main()
