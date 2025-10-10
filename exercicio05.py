import errors_check

def dec_to_hex(decimal : int) -> str:
    char_table : dict[int, str] = {
        0 : '0', 1 : '1', 2 : '2', 3 : '3', 4 : '4',
        5 : '5', 6 : '6', 7 : '7', 8 : '8', 9 : '9',
        10 : 'A', 11 : 'B', 12 : 'C', 13 : 'D', 14 : 'E',
        15 : 'F',
    }
    entry_charset : dict[str, int] = {
        '0' : 0, '1' : 1, '2' : 2, '3' : 3, '4' : 4,
        '5' : 5, '6' : 6, '7' : 7, '8' : 8, '9' : 9,
        '-' : None,
    }
    result : str = str()
    negative : bool = False

    errors_check.check_charset(entry_charset, str(decimal))
    errors_check.check_signal_placement(str(decimal))
    decimal = int(decimal)
    
    if (decimal == 0):
        return str(0)

    if (decimal < 0):
        negative = True
        decimal = abs(decimal)
    
    while (decimal > 0):
        digit : int = decimal % 16
        result += char_table[digit]
        decimal //= 16
    
    if (negative):
        result += '-'
    
    return result[::-1]

def main() -> None:
    try:
        num = input('> ')
        print(dec_to_hex(num))
    except Exception as error:
        print(f'Uncaught error: {error}, {type(error)}')

    return None

if __name__ == '__main__':
    main()
