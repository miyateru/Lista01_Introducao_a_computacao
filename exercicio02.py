import errors

def bin_to_dec(b : str) -> int:
    """
    Converts a binary number to a decimal number.
    """
    errors.in_base(b, 2)
    errors.signal_placement(b)

    negative : bool = False
    if ('-' in b):
        negative = True
        b = b.replace('-', '')

    # Get's decimal via sucessive multiplication
    decimal : int = int()
    b = b[::-1]
    for i in range(len(b)):
        decimal += int(b[i]) * (2 ** i)
    
    if (negative):
        decimal *= -1

    return decimal

def _main () -> None:
    try:
        num = input("> ")
        print(bin_to_dec(num))
    except errors.OutOfBase:
        print("Entrada não é um numero binário.")
    except errors.IncorrectSignalPlacement:
        print("Sinal negativo em posição incorreta.")
    except errors.IncorrectWhitespace:
        print("Uso incorreto de tabulação e/ou espaço em branco dentro do número.")
    except errors.IncorrectSymbol:
        print("Símbolo desconhecido ou não suportado usado.")
    except KeyboardInterrupt:
        exit()
    except Exception as error:
        print(f"Erro não previsto: {error}, Tipo: {type(error)}")

    return None

if __name__ == "__main__":
    _main()
