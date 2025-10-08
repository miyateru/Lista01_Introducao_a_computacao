def convert_base(num : str, base_from : int = 10, base_to : int = 10) -> str:
    resultado : str = ""
    
    # Ver se o sinal é negativo
    negativo: bool = False
    if "-" in num:
        negativo = True
        num = num.replace("-", "")
    
    # Trata bases diferentes para o sistema decimal
    num_decimal : int = 0
    num = num[::-1]
    for N in range(len(num)):
        if base_from > 10 and num[N].isalpha():
            num_decimal += (ord(num[N]) - ord('A') + 10) * (base_from ** N)
        else:
            num_decimal += int(num[N]) * (base_from ** N)

    for char in str(num_decimal):
        resultado += char

    # if base_from == base_to:
    #     return num
    # # base_from -> base_to
    # elif base_from == 10:
    #     int_num : int = int(num) 
        
    #     while int_num > 0:
    #         posicao : int = ord('A')
    #         parcela : int = int_num % base_to
            
    #         if parcela >= 10:
    #             while posicao < (parcela - 10) + ord('A'):
    #                 posicao += 1
    #             resultado += chr(posicao)
    #         else:
    #             resultado += str(int_num % base_to)
                
    #         int_num //= base_to
        
    #     if (negativo):
    #         resultado = '-' + resultado
    # base_from -> base_10 -> base_to
    #else:
        # base_to < 10
        # int_num : int = int(num) 
        # decimal += num * (base_to ** posicao_index)
        # base_to > 10
        #else:
        #    print("Não :p")

    return resultado
  
def main () -> None:
    num : str = input("Numero a ser convertido: ")
    base_to : int = int(input("Da base: "))
    base_from : int = int(input("Para a base: "))
    
    print(convert_base(num, base_to, base_from))

    return None

if __name__ == "__main__":
    main()