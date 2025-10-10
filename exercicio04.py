import errors_check

def oct_to_dec(octal : str) -> int:
    entry_charset : dict[str : int] = {
        '0' : 0, '1' : 1, '2' : 2, '3' : 3, '4' : 4,
        '5' : 5, '6' : 6, '7' : 7, '8' : 8, '9' : 9,
        '-' : None,
    }
    decimal : int = 0
    negative : bool = False

    errors_check.check_charset(entry_charset, octal)
    errors_check.check_signal_placement(octal)
  
    if ("-" in octal):
        negative = True
        octal = octal.replace("-", "")

    octal = octal[::-1]
    
    for N in range(len(octal)):
        decimal += int(octal[N]) * (8 ** N)
    
    if negative:
        decimal *= -1

    return decimal

def main () -> None:
    try:
        num = input("> ")
        print(oct_to_dec(num))
    except Exception as error:
        print(f"Uncaught error: {error}", {type(error)})
        
    return None

if __name__ == "__main__":
    main()
