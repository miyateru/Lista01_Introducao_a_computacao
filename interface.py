#COLOCA O TREM DE LINUX AQUI DNV !!!!
# -*- coding: utf-8 -*-
import platform
from exercicio01 import dec_to_bin
from exercicio02 import bin_to_dec
from exercicio03 import dec_to_oct
from exercicio04 import oct_to_dec
from exercicio05 import dec_to_hex
from exercicio06 import hex_to_dec
from exercicio07 import convert_base
from os import system
from time import sleep
# from automated_tests import 

def chooseNumber() -> int:
    num : int = int(input("> Número a ser convertido: "))
    return num

def clearTerminal() -> None:
    if (platform.system() == "Windows"):
        system("cls")
    else:
        system("clear")

def printLine() -> None:
    print("*", "-" * 100, "*")

def option1() -> None:
    entry_text : str = """
> Seja bem vindo a escolha manual de conversão de bases numéricas!
> Por favor, escolha um tipo de conversão: 

    0. Voltar para o menu principal
    1. Decimal para binário
    2. Binário para decimal
    3. Decimal para octal
    4. Octal para decimal
    5. Decimal para hexadecimal
    6. Hexadecimal para decimal
    7. Conversão genérica de bases
    8. Decimal fracionário para binário fracionário
    9. Binário fracionário para Decimal fracionário
    10. Formatação e largura fixa 
    """
    clearTerminal()
    printLine()
    print(entry_text)

    escolha = int(input("Digite sua escolha: "))
    printLine()

    if (escolha == 1):
        clearTerminal()
        print("1. Decimal para Binário \n")
        
        dec : int = chooseNumber()
        print("> Número convertido:", dec_to_bin(dec))

    elif (escolha == 2):
        clearTerminal()
        print("2. Binário para decimal \n")
        
        bin : str = str(chooseNumber())
        print("> Número convertido:", bin_to_dec(bin))
    
    elif (escolha == 3):
        clearTerminal()
        print("3. Decimal para octal \n")
        
        dec = chooseNumber()
        print("> Número convertido:", dec_to_oct(dec))

    elif (escolha == 4):
        clearTerminal()
        print("4. Octal para decimal \n")
        
        oct : str = str(chooseNumber())
        print("> Número convertido:", oct_to_dec(oct))

    elif (escolha == 5):
        clearTerminal()
        print("5. Decimal para hexadecimal \n")
        
        dec = chooseNumber()
        print("> Número convertido:", dec_to_hex(dec))

    elif (escolha == 6):
        clearTerminal()
        print("6. Hexadecimal para decimal \n")
        
        hex : str = str(chooseNumber())
        print("> Número convertido:", hex_to_dec(hex))
    
    elif (escolha == 7):
        clearTerminal()
        print("7. Conversão genérica de bases \n")
        
        num : str = str(chooseNumber())
        base_to : int = int(input("> Escolha a base original do número: "))
        base_from : int = int(input("> Escolha a base que o número será convertido: "))
        print("> Número convertido:", convert_base(num, base_to, base_from))

    else:
        print("Entrada inválida e/ou exercício ainda não feito!")

    return None

def interface () -> None:
    printLine()

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
        print("Escolha inválida!\nRetornando ao menu principal.")
        sleep(2)
        interface()


    return None

if __name__ == "__main__":
    interface()
