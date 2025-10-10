import errors_check

def dec_to_bin(decimal : int) -> str:
    entry_charset : dict[str : int] = {
        '0' : 0, '1' : 1, '2' : 2, '3' : 3, '4' : 4,
        '5' : 5, '6' : 6, '7' : 7, '8' : 8, '9' : 9,
        '-' : None,
    }
    negative : bool = False
    result : str = str()

    errors_check.check_charset(entry_charset, str(decimal))
    errors_check.check_signal_placement(str(decimal))
    decimal = int(decimal)

    if (decimal == 0):
        return str(0)
  
    if (decimal < 0):
        negative = True
        decimal = abs(decimal)
    
    while (decimal > 0):
        result += str(decimal % 2)
        decimal //= 2
    
    if (negative):
        result += '-'
    
    return result[::-1]

def main() -> None:
    try:
        num = input("> ")
        print(dec_to_bin(num))
    except Exception as error:
        print(f"Uncaught error: {error}", {type(error)})

    return None

if __name__ == "__main__":
    main()
