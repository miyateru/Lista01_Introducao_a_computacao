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
from exercicio08 import decfrac_to_bin
from os import system
from time import sleep
# from automated_tests import algoKKKKK

timer : int = 1

def chooseNumber() -> int:
    num : int = int(input("    > Número a ser convertido: "))
    return num

def conversionComplete() -> str:
    text : str = "    > Número convertido:"
    return text

def retry() -> None:
    sleep(timer)

    print("\n> Gostaria de realizar outra conversão?")

    option = str(input("\nDigite sua escolha (S/N): "))
    option = option.upper()

    if (option == 'S'):
        print ("> Retornando ao menu de opções...")
        clearTerminal()
        option1()

    else:
        print ("> Retornando ao menu principal...")
        clearTerminal()
        interface()

def clearTerminal() -> None:
    if (platform.system() == "Windows"):
        system("cls")
    else:
        system("clear")

def printLine() -> None:
    print("*", "-" * 100, "*")

def option1() -> None:
    clearTerminal()
    printLine()

    entry_text : str = """
> Seja bem vindo(a) a escolha manual de conversão de bases numéricas!
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

    print(entry_text)

    option = int(input("Digite sua escolha: "))

    if (option == 0):
        print("\n> Voltando ao menu principal...")
        sleep(timer)
        clearTerminal()
        interface()

    elif (option == 1):
        clearTerminal()
        print("1. Decimal para Binário \n")
        
        dec : int = chooseNumber()
        print(conversionComplete(), dec_to_bin(dec))
        retry()

    elif (option == 2):
        clearTerminal()
        print("2. Binário para decimal \n")
        
        bin : str = str(chooseNumber())
        print(conversionComplete(), bin_to_dec(bin))
        retry()
    
    elif (option == 3):
        clearTerminal()
        print("3. Decimal para octal \n")
        
        dec = chooseNumber()
        print(conversionComplete(), dec_to_oct(dec))
        retry()

    elif (option == 4):
        clearTerminal()
        print("4. Octal para decimal \n")
        
        oct : str = str(chooseNumber())
        print(conversionComplete(), oct_to_dec(oct))
        retry()

    elif (option == 5):
        clearTerminal()
        print("5. Decimal para hexadecimal \n")
        
        dec = chooseNumber()
        print(conversionComplete(), dec_to_hex(dec))
        retry()

    elif (option == 6):
        clearTerminal()
        print("6. Hexadecimal para decimal \n")
        
        hex : str = str(chooseNumber())
        print(conversionComplete(), hex_to_dec(hex))
        retry()

    elif (option == 7):
        clearTerminal()
        print("7. Conversão genérica de bases \n")
        
        num : str = str(chooseNumber())
        base_to : int = int(input("    > Escolha a base original do número: "))
        base_from : int = int(input("    > Escolha a base que o número será convertido: "))
        print(conversionComplete(), convert_base(num, base_to, base_from))
        retry()

    elif (option == 8):
        clearTerminal()
        print("8. Decimal fracionário para binário fracionário")

        dec : float = float(chooseNumber())
        max_frac : int = int(input("    > Escolha a precisão da parte fracionária: "))
        print (conversionComplete(), decfrac_to_bin(num, max_frac))
        retry()

    elif (option == 9):
        clearTerminal()
        print("9. Binário fracionário para Decimal fracionário")

        bin = str(chooseNumber())
        print("\nExercício ainda não feito!")
        retry()

    elif (option == 10):
        clearTerminal()
        print("10. Formatação e largura fixa")

        print("\nainda nao ta feitooo!!!!")
        retry()

    else:
        print("Entrada inválida!\n Retornando...")
        sleep(timer)
        clearTerminal()
        option1()

    return None

def interface () -> None:
    printLine()

    main_text : str = """
> Olá, e seja bem vindo(a) ao programa de conversão de bases numéricas!
> Por favor, escolha uma opção: 

    1. Escolha manual de conversão
    2. Testes automatizados
    3. Sair do programa
"""

    print(main_text)

    option : int = int(input("Digite sua escolha: "))

    if (option == 1):
        option1()

    elif (option == 2):
        clearTerminal()
        printLine()
        print("Testes ainda incompletos!\nGostaria de retornar ao menu principal?")

        option = str(input("\nEscolha (S/N): "))
        option = option.upper()

        if (option == 'S'):
            sleep(timer)
            clearTerminal()
            interface()

        else:
            print("> Saindo...")
            sleep(timer)
            exit()

    elif (option == 3):
        print("> Saindo...")
        sleep(timer)
        exit()
    
    else:
        print("Escolha inválida!\nRetornando ao menu principal...")
        sleep(timer)
        clearTerminal()
        interface()

    return None

if __name__ == "__main__":
    interface()
