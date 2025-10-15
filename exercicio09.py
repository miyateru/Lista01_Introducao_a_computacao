import errors

def binfrac_to_dec(b : str) -> float:
    """
    Converts a fractional binary number into a decimal number.
    """
    errors.in_base(b, 2, True)
    errors.signal_placement(b)
    
    negative : bool = False
    if ('-' in b):
        negative = True
        b = b.replace('-', '')
    
    index_separator : int = b.find(".")
    int_part : str = str(b[:index_separator:])
    float_part : str = str(b[index_separator + 1::])
    result : float = float()
    
    if (len(int_part) == 0) or (len(float_part) == 0):
        raise FloatingPointError
    
    # Get's integer decimal part via sucessive multiplication
    int_part = int_part[::-1]
    for i in range(len(int_part)):
        result += int(int_part[i]) * (2 ** i)
        
    # Get's fractional part via sucessive multiplication
    # By negative potencies of two
    for i in range(1, len(float_part) + 1):
        result += int(float_part[i - 1]) * (1/2 ** i)
    
    if negative:
        result *= -1
    
    return result

def _main () -> None:
    try:
        num = input("> ")
        print(binfrac_to_dec(num))
    except errors.OutOfBase:
        print("Entrada não é um numero binário.")
    except errors.IncorrectSignalPlacement:
        print("Sinal negativo em posição incorreta.")
    except FloatingPointError:
        print("Número não é flutuante.")
    except errors.IncorrectWhitespace:
        print("Uso incorreto de tabulação e/ou espaço em branco dentro do número.")
    except errors.IncorrectSymbol:
        print("Símbolo desconhecido ou não suportado usado.")
    except Exception as error:
        print(f"Erro não previsto: {error}, Tipo: {type(error)}")

    return None

if __name__ == "__main__":
    _main()
