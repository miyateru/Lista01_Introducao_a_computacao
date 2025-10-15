import errors

def oct_to_dec(o : str) -> int:
    """
    Converts a octal number to a decimal number.
    """
    errors.in_base(o, 8)
    errors.signal_placement(o)
  
    negative : bool = False
    if ("-" in o):
        negative = True
        o = o.replace("-", "")

    # Get's octal via sucessive multiplication
    decimal : int = int()
    o = o[::-1]
    for i in range(len(o)):
        decimal += int(o[i]) * (8 ** i)
    
    if (negative):
        decimal *= -1

    return decimal

def _main () -> None:
    try:
        num = input("> ")
        print(oct_to_dec(num))
    except errors.OutOfBase:
        print("Entrada não é um numero octal.")
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
