#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Decimal inteiro → Binário (método das divisões sucessivas) 
def dec_to_hex(n: int) -> str:
    resultado : str = ""
    equivalencia : dict[int, str] = {
        0 : '0',
        1 : '1',
        2 : '2',
        3 : '3',
        4 : '4',
        5 : '5',
        6 : '6',
        7 : '7',
        8 : '8',
        9 : '9',
        10 : 'A',
        11 : 'B',
        12 : 'C',
        13 : 'D',
        14 : 'E',
        15 : 'F',
    }
    
    if (n == 0):
        return str(0)
    
    # Ver a posicao do sinal
    negativo : bool = False
    if n < 0:
        negativo = True
        n = abs(n)
    
    while (n > 0):
        num : int = n % 16
        resultado += equivalencia[num]
        n //= 16
    
    if (negativo):
        resultado += '-'
    
    return resultado[::-1]

def main() -> None:
    num = int(input("> "))
    print(dec_to_hex(num))

    return None

if __name__ == "__main__":
    main()
