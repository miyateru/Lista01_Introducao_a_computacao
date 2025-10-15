import errors

def hex_to_int(h : str) -> int:
    if (ord(h) >= ord('A') and ord(h) <= ord('F')):
        return (ord(h) - ord('A')) + 10
    return ord(h) - ord('0') 

def hex_to_dec(h : str) -> int:
    """
    Converts a hexadecimal number to a decimal number.
    """
    h = h.upper()
    errors.in_base(h, 16)
    errors.signal_placement(h)

    negative : bool = False
    if ('-' in h):
        negative = True
        h = h.replace("-", "")
    
    # Get's hexadecimal via sucessive multiplication
    decimal : int = int()
    h = h[::-1]
    for i in range(len(h)):
        decimal += hex_to_int(h[i]) * (16 ** i)

    if (negative):
        decimal *= -1

    return decimal

def _main () -> None:
    try:
        num = input("> ")
        print(hex_to_dec(num))
    except errors.OutOfBase:
        print("Entrada não é um numero hexadecimal.")
    except errors.IncorrectSignalPlacement:
        print("Sinal negativo em posição incorreta.")
    except errors.IncorrectWhitespace:
        print("Uso incorreto de tabulação e/ou espaço em branco dentro do número.")
    except errors.IncorrectSymbol:
        print("Símbolo desconhecido ou não suportado usado.")
    except Exception as error:
        print(f"Erro não previsto: {error}, Tipo: {type(error)}")
        
    return None

if __name__ == "__main__":
    _main()
