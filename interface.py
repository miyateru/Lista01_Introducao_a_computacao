#COLOCA O TREM DE LINUX AQUI DNV !!!!
# -*- coding: utf-8 -*-
import os
from exercicio01 import dec_to_bin
from exercicio02 import bin_to_dec
from exercicio03 import dec_to_oct
from exercicio04 import oct_to_dec
from exercicio05 import dec_to_hex
from exercicio06 import hex_to_dec
from exercicio07 import convert_base
# from automated_tests import 

def chooseNumber() -> int:
    num : int = int(input("> Número a ser convertido: "))
    return num

def option1() -> None:
    #acho que em linux o comando muda, mas meu python nao ta funcionando por la, entao vai no windows mesmo
    #lembra de mudar isso pra 'clear' eu acho, possivelmente :p
    os.system('cls')
    print ("*", "-" * 30, "*")

    print("> Seja bem vindo a escolha manual de conversão de bases numéricas!")
    print("> Por favor, escolha um tipo de conversão: \n")

    print("1. Decimal para binário")
    print("2. Binário para decimal")
    print("3. Decimal para octal")
    print("4. Octal para decimal")
    print("5. Decimal para hexadecimal")
    print("6. Hexadecimal para decimal")
    print("7. Conversão genérica de bases")
    print("8. EM ANDAMENTO - ARRUMA ISSO DEPOIS !!!! \n")

    escolha = int(input("Digite sua escolha: "))
    print ("*", "-" * 30, "* \n")

    if (escolha == 1):
        os.system('cls')
        print("1. Decimal para Binário \n")
        
        dec : int = chooseNumber()
        print("> Número convertido:", dec_to_bin(dec))

    elif (escolha == 2):
        os.system('cls')
        print("2. Binário para decimal \n")
        
        bin : str = str(chooseNumber())
        print("> Número convertido:", bin_to_dec(bin))
    
    elif (escolha == 3):
        os.system('cls')
        print("3. Decimal para octal \n")
        
        dec = chooseNumber()
        print("> Número convertido:", dec_to_oct(dec))

    elif (escolha == 4):
        os.system('cls')
        print("4. Octal para decimal \n")
        
        oct : str = str(chooseNumber())
        print("> Número convertido:", oct_to_dec(oct))

    elif (escolha == 5):
        os.system('cls')
        print("5. Decimal para hexadecimal \n")
        
        dec = chooseNumber()
        print("> Número convertido:", dec_to_hex(dec))

    elif (escolha == 6):
        os.system('cls')
        print("6. Hexadecimal para decimal \n")
        
        hex : str = str(chooseNumber())
        print("> Número convertido:", hex_to_dec(hex))
    
    elif (escolha == 7):
        os.system('cls')
        print("7. Conversão genérica de bases \n")
        
        num : str = str(chooseNumber())
        base_to : int = int(input("> Escolha a base original do número: "))
        base_from : int = int(input("> Escolha a base que o número será convertido: "))
        print("> Número convertido:", convert_base(num, base_to, base_from))

    else:
        print("Entrada inválida e/ou exercício ainda não feito!")

    return None

def interface () -> None:
    print ("*", "-" * 30, "*")

    print("\n> Olá, e seja bem vindo(a) ao programa de conversão de bases numéricas!")
    print("> Por favor, escolha uma opção: \n")

    #escolha manual das bases -> os exercicios
        #se foi esse o escolhido, aí passa para os exercícios
    print("1. Escolha manual de conversão")
    
    #escolha automatizada -> alguns aí sei la nao faço ideiaKKKKK
    print("2. Testes automatizados")

    escolha : int = int(input("Digite sua escolha: "))

    if (escolha == 1):
        option1()

    elif (escolha == 2):
        print("Testes ainda incompletos!")
    
    else:
        #eu nao faco ideia de como resetar pro negocio em cima dnv KKKK dps eu vejo isso
        print("Escolha inválida!")

    return None

if __name__ == "__main__":
    interface()