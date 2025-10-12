import errors_check

def oct_to_dec(octal : str) -> int:
    entry_charset : dict[str, int | None] = {
        '0' : 0, '1' : 1, '2' : 2, '3' : 3, '4' : 4,
        '5' : 5, '6' : 6, '7' : 7, '8' : 8,
        '-' : None,
    }
    decimal : int = 0
    negative : bool = False

    errors_check.charset(entry_charset, octal)
    errors_check.signal_placement(octal)
  
    if ("-" in octal):
        negative = True
        octal = octal.replace("-", "")

    # Get's octal via sucessive multiplication
    octal = octal[::-1]
    for N in range(len(octal)):
        decimal += int(octal[N]) * (8 ** N)
    
    if negative:
        decimal *= -1

    return decimal

def main () -> None:
    try:
        num = input("> ")
        # Considering non-sanitized input
        print(oct_to_dec(num))
    except errors_check.invalid_charset:
        print("Entrada não é um numero octal.")
    except errors_check.invalid_syntax:
        print("Sinal negativo em posição incorreta.")
    except Exception as error:
        print(f"Erro não previsto: {error}, Tipo: {type(error)}")
    return None

if __name__ == "__main__":
    main()
