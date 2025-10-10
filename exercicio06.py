import errors_check

def hex_to_dec(hexadecimal : str) -> int:
    char_table : dict[str, int] = {
        '0' : 0, '1' : 1, '2' : 2, '3' : 3, '4' : 4,
        '5' : 5, '6' : 6, '7' : 7, '8' : 8, '9' : 9,
        '-' : None,
    }
    entry_charset : dict[int, str] = {
        0 : '0', 1 : '1', 2 : '2', 3 : '3', 4 : '4',
        5 : '5', 6 : '6', 7 : '7', 8 : '8', 9 : '9',
        10 : 'A', 11 : 'B', 12 : 'C', 13 : 'D', 14 : 'E',
        15 : 'F',
    }
    decimal : int = 0
    negative : bool = False

    hexadecimal = hexadecimal.upper()

    errors_check.check_charset(entry_charset, hexadecimal)
    errors_check.check_signal_placement(hexadecimal)

    if ('-' in hexadecimal):
        negative = True
        hexadecimal = hexadecimal.replace("-", "")

    hexadecimal = hexadecimal[::-1]
    
    for N in range(len(hexadecimal)):
        decimal += char_table[hexadecimal[N]] * (16 ** N)

    if negative:
        decimal *= -1

    return decimal

def main () -> None:
    try:
        num = input('> ')
        print(hex_to_dec(num))
    except Exception as error:
        print(f'Uncaught error: {error}, {type(error)}')

    return None

if __name__ == "__main__":
    main()
