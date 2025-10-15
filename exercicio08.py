import errors
from math import trunc

def decfrac_to_bin(num : float, max_frac_bits : int = 16) -> str:
    """
    Converts a fractional decimal number to a fractional binary number.
    """
    errors.in_base(str(num), 10, True)
    errors.signal_placement(str(num))
    num = float(num)
    
    #Handles the integer part of the number
    num_int : int = trunc(num)

    negative : bool = False
    if (num_int < 0):
        negative = True
        num_int = abs(num_int)
        
    result_int : str = str()    
    while (num_int > 0):
        result_int += str(num_int % 2)
        num_int //= 2
    
    if (negative):
        result_int += '-'

    #Handles the float part of the number
    num_frac : str = str(num % 1)
    result_frac : str = str()

    ## Removes the trailing 0 and dot
    num_frac = num_frac[2::]
    frac_as_num : int = int(num_frac)
    while ((frac_as_num > 0) and (len(result_frac) < max_frac_bits)):
        result_frac += str(frac_as_num % 2)
        frac_as_num //= 2

    return f"{result_int[::-1]}.{result_frac[::-1]}"

def _main () -> None:
    try:
        num : float = float(input("Número a ser convertido: "))
        max_frac : int = int(input("Precisão da parte fracionária: "))

        print(decfrac_to_bin(num, max_frac))
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

    return None

if __name__ == "__main__":
    _main()
    