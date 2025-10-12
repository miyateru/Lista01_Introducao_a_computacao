import errors_check

def dec_to_bin(decimal : int) -> str:
    entry_charset : dict[str, int | None] = {
        '0' : 0, '1' : 1, '2' : 2, '3' : 3, '4' : 4,
        '5' : 5, '6' : 6, '7' : 7, '8' : 8, '9' : 9,
        '-' : None,
    }
    binary : str = str()
    negative : bool = False

    errors_check.charset(entry_charset, str(decimal))
    errors_check.signal_placement(str(decimal))
    decimal = int(decimal)

    if (decimal == 0):
        return str(0)
  
    if (decimal < 0):
        negative = True
        decimal = abs(decimal)
    
    # Gets the binary using sucessive divisions (result comes inverted)
    while (decimal > 0):
        binary += str(decimal % 2)
        decimal //= 2
    
    if (negative):
        binary += '-'
    
    return binary[::-1]

def main() -> None:
    try:
        num = input("> ")
        # Considering non-sanitized input, warning is being supressed
        print(dec_to_bin(num)) # type: ignore
    except errors_check.invalid_charset:
        print("Entrada não é um numero decimal.")
    except errors_check.invalid_syntax:
        print("Sinal negativo em posição incorreta.")
    except Exception as error:
        print(f"Erro não previsto: {error}, Tipo: {type(error)}")

    return None

if __name__ == "__main__":#
    main()
