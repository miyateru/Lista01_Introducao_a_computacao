import errors

def convert_base(num : str, base_from : int = 10, base_to : int = 10) -> str:
    """
    Converts a number from a given base to a number in the other given base.
    """
    errors.in_base(num, base_from)
    errors.signal_placement(num)
    num = num.upper()

    negative : bool = False
    if ('-' in num):
        negative = True
        num = num.replace('-', '')
    
    # base_from -> base decimal (10)
    num_decimal : int = int()
    num = num[::-1]
    for i in range(len(num)):
        if (base_from > 10 and num[i].isalpha()):
            num_decimal += (ord(num[i]) - ord('A') + 10) * (base_from ** i)
        else:
            num_decimal += int(num[i]) * (base_from ** i)

    #Converter de decimal para a base escolhida (base_to)
    result : str = str()
    while num_decimal > 0:
        num_base : int =  num_decimal % base_to
        num_decimal //= base_to

        if num_base > 10:
            result += str(int(ord('A') + num_decimal - 10))
        else:
            result += str(num_base)

    if (negative):
        result += '-'

    return result[::-1]

def _main () -> None:
    try:
        num : str = input("Número a ser convertido: ")
        base_to = (input("Da base: "))
        base_from  = (input("Para a base: "))
        # Considering non-sanitized input
        print(convert_base(num, base_to, base_from)) # type: ignore
    except errors.OutOfBase:
        print("O numero não esta na base de entrada informada.")
    except errors.IncorrectSignalPlacement:
        print("Sinal negativo em posição incorreta")
    except errors.IncorrectWhitespace:
        print("Uso incorreto de tabulação e/ou espaço em branco dentro do número.")
    except errors.IncorrectSymbol:
        print("Símbolo desconhecido ou não suportado usado.")
    except ValueError:
        print("Base inválida.")
    except Exception as error:
        print(f"Erro não previsto: {error}, Tipo: {type(error)}")

    return None

if __name__ == "__main__":
    _main()
