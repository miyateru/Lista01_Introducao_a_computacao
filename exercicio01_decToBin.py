#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Decimal inteiro → Binário (método das divisões sucessivas) 
def dec_to_bin(n: int) -> str:
    resultado : str = ""
    
    if (n == 0):
        return str(0)
    
    # Ver a posicao do sinal
    negativo : bool = False
    if n < 0:
        negativo = True
        n = abs(n)
    
    while (n > 0):
        resultado += str(n % 2)
        n //= 2
    
    if (negativo):
        resultado += '-'
    
    return resultado[::-1]

def main():
    num = input("> ")
    
    try:
        num = float(num)
        print(dec_to_bin(int(num)))
    except ValueError:
        print("Valor invalido.")
    except TypeError:
        print("Tipo invalido.")
    except OverflowError:
        print("Valor excede o maximo. Muito grande :(")
    except ExceptionGroup as error:
        print(f"Não especificado. Error: {error}")

if __name__ == "__main__":
    main()
