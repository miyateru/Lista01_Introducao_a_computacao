import errors_check

def bin_to_dec(b: str) -> int:
    decimal : int = 0
    negative : bool = False
    valid_charset : list[str] = ['-', '0', '1']

    errors_check.check_charset(valid_charset, b)
    errors_check.check_signal_placement(b)

    if '-' in b:
        negative = True
        b = b.replace('-', "")

    b = b[::-1]

    for N in range(len(b)):
        decimal += int(b[N]) * (2 ** N)
    
    if negative:
        decimal *= (-1)

    return decimal

def main () -> None:
    try:
        num = input("> ")
        print(bin_to_dec(num))
    except Exception as error:
        print(f"Uncaught error: {error}", {type(error)})

    return None

if __name__ == "__main__":
    main()
