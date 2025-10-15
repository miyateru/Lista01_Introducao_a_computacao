class IncorrectSignalPlacement(SyntaxError):
    """
    The placement of some mathematical expression is incorrect.
    """
    pass

class IncorrectSymbol(SyntaxError):
    """
    Usage of symbol that is not recognized and/or implemented.
    """

class IncorrectWhitespace(SyntaxError):
    """
    The placement of tabulation and/or whitespace is incorrect.
    """
    pass

class OutOfBase(ValueError):
    """
    Not in the correct number base.
    """
    pass

def in_base(num : str, base : int = 10, frac : bool = False) -> None:
    """    
    Check if a given number is in the given base.\n
    Returns None if number is in base. Otherwise raises an Exception.\n
    For any base greater than 10 utilizes letters from A up to Z (min base: 0, max base: 36).\n
    Ignores the negative or positive symbol. Ignores dots if frac flag (the third argument) is true.\n
    Is 0 indexed.\n
    """
    if ((base < 0) or (base > 36)):
        raise SyntaxError("Base min: 0, Base max: 36")
    
    for char in num:
        ignored : list[str] = ['-', '+']
        if (frac):
            ignored.append('.')
        zero_to_nine : bool = (ord(char) >= ord('0')) and (ord(char) <= ord('9'))
        A_to_Z : bool = ((ord(char) >= ord('A')) and (ord(char) <= ord('Z')) or
                         (ord(char) >= ord('a')) and (ord(char) <= ord('z')))
        
        if (char in ignored):
            continue
        elif (zero_to_nine):
            if (int(char) > base or int(char) < 0):
                raise OutOfBase("Número não está na base informada.")
        elif (A_to_Z):
            if ((ord(char) - ord('A')) + 11 > base):
                raise OutOfBase("Número não está na base informada.")
        elif ((char == '\t') or (char == ' ')):
            raise IncorrectWhitespace("Utilização de tabulação e/ou espaço dentro do número.")
        elif (not zero_to_nine) and (not A_to_Z) and (char not in ignored):
            raise IncorrectSymbol("Símbolo desconhecido ou não suportado.")
        else:
            continue
        
    return None

def signal_placement(vector : str) -> None:
    """
    Check if the negative signal of a number is in the correct place.\n
    Return None if it's correct. Otherwise returns IncorrectSignalPlacement Excepection.\n
    """
    if ('-' in vector) and (0 != vector.index('-')):
            raise IncorrectSignalPlacement("O sinal de negativo deve estar no começo do número.")
    return None

def main():
    try:
        num : str = input("Número: ")
        base_to : int = int(input("Base: "))
        in_base(num, base_to)
        signal_placement(num)
    except OutOfBase:
        print("O numero não esta na base de entrada informada.")
    except IncorrectSignalPlacement:
        print("Sinal negativo em posição incorreta")
    except IncorrectWhitespace:
        print("Uso incorreto de tabulação e/ou espaço em branco dentro do número.")
    except IncorrectSymbol:
        print("Símbolo desconhecido ou não suportado usado.")
    except Exception as error:
        print(f"Erro não previsto: {error}, Tipo: {type(error)}")
    else:
        print("Numero corretamente formatado.")

if __name__ == "__main__":
    main()
