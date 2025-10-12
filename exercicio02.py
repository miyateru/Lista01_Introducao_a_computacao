import errors_check

def bin_to_dec(binary : str) -> int:
    entry_charset : dict[str, int | None] = {
        '0' : 0, '1' : 1, '-' : None,
    }
    decimal : int = 0
    negative : bool = False

    errors_check.charset(entry_charset, binary)
    errors_check.signal_placement(binary)

    if ('-' in binary):
        negative = True
        binary = binary.replace('-', "")

    # Get's decimal via sucessive multiplication
    binary = binary[::-1]
    for N in range(len(binary)):
        decimal += int(binary[N]) * (2 ** N)
    
    if (negative):
        decimal *= -1

    return decimal

def main () -> None:
    try:
        num = input("> ")
        # Considering non-sanitized input
        print(bin_to_dec(num))
    except errors_check.invalid_charset:
        print("Entrada não é um numero binário.")
    except errors_check.invalid_syntax:
        print("Sinal negativo em posição incorreta.")
    except Exception as error:
        print(f"Erro não previsto: {error}, Tipo: {type(error)}")

    return None

if __name__ == "__main__":
    main()
