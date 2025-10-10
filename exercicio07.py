def convert_base(num : str, base_from : int = 10, base_to : int = 10) -> str:
    resultado : str = ""
    
    # Converter as entradas que possuem letras para maiúsculas
    num = num.upper()

    # Ver se o número é negativo
    negative : bool = False
    if "-" in num:
        negative = True
        num = num.replace("-", "")
    
    # base_from -> base decimal (10)
    num_decimal : int = 0
    num = num[::-1]
    for N in range(len(num)):
        if base_from > 10 and num[N].isalpha():
            num_decimal += (ord(num[N]) - ord('A') + 10) * (base_from ** N)
        else:
            num_decimal += int(num[N]) * (base_from ** N)

    #Converter de decimal para a base escolhida (base_to)
    while num_decimal > 0:
        num_base : int =  num_decimal % base_to
        num_decimal //= base_to

        if num_base > 10:
            resultado += str(int(ord('A') + num_decimal - 10))
        else:
            resultado += str(num_base)

    if negative:
        resultado += '-'

    return resultado[::-1]

def main () -> None:
    num : str = input("Número a ser convertido: ")
    base_to : int = int(input("Da base: "))
    base_from : int = int(input("Para a base: "))
    
    print(convert_base(num, base_to, base_from))

    return None

if __name__ == "__main__":
    main()