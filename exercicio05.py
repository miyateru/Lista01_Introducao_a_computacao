import errors

def int_to_hex(n : int) -> str:
    if (n >= 10):
        result : str = str()
        result = chr(ord('A') + (n - 10))
        return result
    
    return str(n)

# Because of type hinting invalid entries should be treated outside the function
# Checking anyway, see in the README the type hinting section
def dec_to_hex(n : int) -> str:
    """
    Converts a decimal number to a hexadecimal number.
    """
    errors.in_base(str(n), 16)
    errors.signal_placement(str(n))
    n = int(n)
    
    if (n == 0):
        return str(0)

    negative : bool = False
    if (n < 0):
        negative = True
        n = abs(n)
    
    # Get's the hecadecimal by using using sucessive divisions (result comes inverted)
    result : str = str()
    while (n > 0):
        result += int_to_hex(n % 16)
        n //= 16
    
    if (negative):
        result += '-'
    
    return result[::-1]

def _main() -> None:
    try:
        num = input("> ")
        # Considering non-sanitized input
        print(dec_to_hex(num)) # type: ignore
    except errors.OutOfBase:
        print("Entrada não é um numero decimal.")
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

if __name__ == '__main__':
    _main()
