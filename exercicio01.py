import errors

# Because of type hinting invalid entries should be treated outside the function
# Checking anyway, see in the README the type hinting section
def dec_to_bin(n : int) -> str:
    """
    Converts a decimal number to a binary number.
    """
    errors.in_base(str(n))
    errors.signal_placement(str(n))
    n = int(n)

    if (n == 0):
        return (str(0))
  
    negative : bool = False
    if (n < 0):
        negative = True
        n = abs(n)
    
    # Gets the binary using sucessive divisions (result comes inverted)
    binary : str = str()
    while (n > 0):
        binary += str(n % 2)
        n //= 2
    
    if (negative):
        binary += '-'
    
    return (binary[::-1])

def _main() -> None:
    try:
        num = input("> ")
        # Considering non-sanitized input
        print(dec_to_bin(num)) # type: ignore
    except errors.OutOfBase:
        print("Entrada não é um numero decimal.")
    except errors.IncorrectSignalPlacement:
        print("Sinal negativo em posição incorreta.")
    except errors.IncorrectWhitespace:
        print("Uso incorreto de tabulação e/ou espaço em branco dentro do número.")
    except errors.IncorrectSymbol:
        print("Símbolo desconhecido ou não suportado usado.")
    except Exception as error:
        print(f"Erro não previsto: {error}, Tipo: {type(error)}")

    return (None)

if __name__ == "__main__":#
    _main()
