import errors_check

def bin_to_dec(binary : str) -> int:
    entry_charset : dict[str : int] = {
        '0' : 0, '1' : 1, '-' : None,
    }
    decimal : int = 0
    negative : bool = False

    errors_check.check_charset(entry_charset, binary)
    errors_check.check_signal_placement(binary)

    if ('-' in binary):
        negative = True
        binary = binary.replace('-', "")

    binary = binary[::-1]

    for N in range(len(binary)):
        decimal += int(binary[N]) * (2 ** N)
    
    if (negative):
        decimal *= -1

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
