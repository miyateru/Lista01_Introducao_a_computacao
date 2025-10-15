#!/usr/bin/env python3
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
from exercicio09 import binfrac_to_dec
from exercicio10 import to_fixed_width_bin, ipv4_to_bin, bin_to_ipv4
from automated_tests import main_test
import errors
from os import system
from time import sleep

timer : int = 2

choose : str = "> Número a ser convertido: "
conversionComplete : str = "> Número convertido:"

def retry() -> None:
    sleep(timer)

    print("\n> Gostaria de realizar outra conversão?")

    option_str = str(input("\nDigite sua escolha (S/N): "))
    option_str = option_str.upper()

    if (option_str == 'S'):
        print ("> Retornando ao menu de opções...")
        clearTerminal()
        option1()
    else:
        print ("> Retornando ao menu principal...")
        clearTerminal()
        interface()
        
    return None

def clearTerminal() -> None:
    if (platform.system() == "Windows"):
        system("cls")
    else:
        system("clear")
        
    return None

def printLine() -> None:
    print("*", "-" * 100, "*")
    
    return None

def backToInterface() -> None:
    print("\n> Voltando ao menu principal...")
    sleep(timer)
    clearTerminal()
    interface()
    
    return None

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

    option : int = int()
    try:
        option = int(input("Digite sua escolha: "))
        if (option < 0) or (option > 10):
            raise(ValueError)
    except ValueError:
        print("Escolha inválida!", end="")
        backToInterface()
    except KeyboardInterrupt:
        exit()
    except Exception as error:
        print(f"Erro não previsto: {error}, Tipo: {type(error)}")

    if (option == 0):
        backToInterface()
        
    elif (option == 1):
        clearTerminal()
        print("1. Decimal para Binário \n")
        
        try:
            decimal = input(choose)
            errors.in_base(decimal)
            errors.signal_placement(decimal)
            decimal = int(decimal)
            print(conversionComplete, dec_to_bin(decimal))
            retry()
        except errors.OutOfBase:
            print("Entrada não é um numero decimal.")
        except errors.IncorrectSignalPlacement:
            print("Sinal negativo em posição incorreta.")
        except errors.IncorrectWhitespace:
            print("Uso incorreto de tabulação e/ou espaço em branco dentro do número.")
        except errors.IncorrectSymbol:
            print("Símbolo desconhecido ou não suportado usado.")
        except ValueError:
            print("Não é um número válido\nVoltando ao menu principal...")
        except KeyboardInterrupt:
            print("Conversão interrompida.")
        except Exception as error:
            print(f"Erro: {error}, Tipo: {type(error)}")
        finally:
            backToInterface()

    elif (option == 2):
        clearTerminal()
        print("2. Binário para decimal \n")
        
        try:
            binary : str = input(choose)
            errors.in_base(binary, 2)
            errors.signal_placement(binary)
            print(conversionComplete, bin_to_dec(binary))
            retry()
        except errors.OutOfBase:
            print("Entrada não é um numero binário.")
        except errors.IncorrectSignalPlacement:
            print("Sinal negativo em posição incorreta.")
        except errors.IncorrectWhitespace:
            print("Uso incorreto de tabulação e/ou espaço em branco dentro do número.")
        except errors.IncorrectSymbol:
            print("Símbolo desconhecido ou não suportado usado.")
        except KeyboardInterrupt:
            print("Conversão interrompida.")
        except Exception as error:
            print(f"Erro: {error}, Tipo: {type(error)}")
        finally:
            backToInterface()
    
    elif (option == 3):
        clearTerminal()
        print("3. Decimal para octal \n")
        
        try:
            decimal = input(choose)
            errors.in_base(decimal)
            errors.signal_placement(decimal)
            decimal = int(decimal)
            print(conversionComplete, dec_to_oct(decimal))
            retry()
        except errors.OutOfBase:
            print("Entrada não é um numero decimal.")
        except errors.IncorrectSignalPlacement:
            print("Sinal negativo em posição incorreta.")
        except errors.IncorrectWhitespace:
            print("Uso incorreto de tabulação e/ou espaço em branco dentro do número.")
        except errors.IncorrectSymbol:
            print("Símbolo desconhecido ou não suportado usado.")
        except KeyboardInterrupt:
            print("Conversão interrompida.")
        except Exception as error:
            print(f"Erro: {error}, Tipo: {type(error)}")
        finally:
            backToInterface()

    elif (option == 4):
        clearTerminal()
        print("4. Octal para decimal \n")
        
        try:
            octal = input(choose)
            errors.in_base(octal, 8)
            errors.signal_placement(octal)
            print(conversionComplete, oct_to_dec(octal))
            retry()
        except errors.OutOfBase:
            print("Entrada não é um numero octal.")
        except errors.IncorrectSignalPlacement:
            print("Sinal negativo em posição incorreta.")
        except errors.IncorrectWhitespace:
            print("Uso incorreto de tabulação e/ou espaço em branco dentro do número.")
        except errors.IncorrectSymbol:
            print("Símbolo desconhecido ou não suportado usado.")
        except KeyboardInterrupt:
            print("Conversão interrompida.")
        except Exception as error:
            print(f"Erro: {error}, Tipo: {type(error)}")
        finally:
            backToInterface()

    elif (option == 5):
        clearTerminal()
        print("5. Decimal para hexadecimal \n")
        
        try: 
            decimal = input(choose)
            errors.in_base(decimal)
            errors.signal_placement(decimal)
            decimal = int(decimal)
            print(conversionComplete, dec_to_hex(decimal))
            retry()
        except errors.OutOfBase:
            print("Entrada não é um numero decimal.")
        except errors.IncorrectSignalPlacement:
            print("Sinal negativo em posição incorreta.")
        except errors.IncorrectWhitespace:
            print("Uso incorreto de tabulação e/ou espaço em branco dentro do número.")
        except errors.IncorrectSymbol:
            print("Símbolo desconhecido ou não suportado usado.")
        except KeyboardInterrupt:
            print("Conversão interrompida.")
        except Exception as error:
            print(f"Erro: {error}, Tipo: {type(error)}")
        finally:
            backToInterface()

    elif (option == 6):
        clearTerminal()
        print("6. Hexadecimal para decimal \n")
        
        try: 
            hexadecimal = input(choose)
            errors.in_base(hexadecimal, 16)
            errors.signal_placement(hexadecimal)
            print(conversionComplete, hex_to_dec(hexadecimal))
            retry()
        except errors.OutOfBase:
            print("Entrada não é um numero hexadecimal.")
        except errors.IncorrectSignalPlacement:
            print("Sinal negativo em posição incorreta.")
        except errors.IncorrectWhitespace:
            print("Uso incorreto de tabulação e/ou espaço em branco dentro do número.")
        except errors.IncorrectSymbol:
            print("Símbolo desconhecido ou não suportado usado.")
        except KeyboardInterrupt:
            print("Conversão interrompida.")
        except Exception as error:
            print(f"Erro: {error}, Tipo: {type(error)}")
        finally:
            backToInterface()

    elif (option == 7):
        clearTerminal()
        print("7. Conversão genérica de bases \n")
        
        try:
            number = input(choose)
            
            base_to = (input("> Digite a base original do número: "))
            if (str(base_to).isnumeric() == False):
                raise errors.NotABase
            base_to = int(base_to)
            
            errors.in_base(number, base_to)
            errors.signal_placement(number)
            
            base_from : int = int(input("> Digite a base que o número será convertido: "))
            if (str(base_from).isnumeric() == False):
                raise errors.NotABase
            base_to = int(base_from)
            
            print(conversionComplete, convert_base(number, base_to, base_from))
            retry()
        except errors.OutOfBase:
            print("O numero não esta na base de entrada informada.")
        except errors.NotABase:
            print("A base deve ser um número")
        except errors.IncorrectSignalPlacement:
            print("Sinal negativo em posição incorreta")
        except errors.IncorrectWhitespace:
            print("Uso incorreto de tabulação e/ou espaço em branco dentro do número.")
        except errors.IncorrectSymbol:
            print("Símbolo desconhecido ou não suportado usado.")
        except ValueError:
            print("Base inválida.")
        except KeyboardInterrupt:
            print("Conversão interrompida.")
        except Exception as error:
            print(f"Erro: {error}, Tipo: {type(error)}")
        finally:
            backToInterface()

    elif (option == 8):
        clearTerminal()
        print("8. Decimal fracionário para binário fracionário")
        
        try:
            decimal = input(choose)
            errors.in_base(decimal, 10, True)
            errors.signal_placement(decimal)
            decimal_frac = float(decimal)
            
            max_frac = input("> Digite a precisão da parte fracionária: ")
            if (str(max_frac).isnumeric() == False):
                raise FloatingPointError("O maximo de numeros deve ser um número inteiro.")
            max_frac = int(max_frac)
            max_frac = int(max_frac)
            
            print(conversionComplete, decfrac_to_bin(decimal_frac, max_frac))
            retry()
        except errors.OutOfBase:
            print("Entrada não é um numero decimal.")
        except errors.IncorrectSignalPlacement:
            print("Sinal negativo em posição incorreta.")
        except errors.IncorrectWhitespace:
            print("Uso incorreto de tabulação e/ou espaço em branco dentro do número.")
        except errors.IncorrectSymbol:
            print("Símbolo desconhecido ou não suportado usado.")
        except FloatingPointError:
            print("O maximo de numeros deve ser um número inteiro.")
        except KeyboardInterrupt:
            print("Conversão interrompida.")
        except Exception as error:
            print(f"Erro não previsto: {error}, Tipo: {type(error)}")
        finally:
            backToInterface()
        
    elif (option == 9):
        clearTerminal()
        print("9. Binário fracionário para Decimal fracionário")

        try:
            binary = input(choose)
            errors.in_base(binary, 2, True)
            errors.signal_placement(binary)
            print(conversionComplete, binfrac_to_dec(binary))
            retry()
        except errors.OutOfBase:
            print("Entrada não é um numero binário.")
        except errors.IncorrectSignalPlacement:
            print("Sinal negativo em posição incorreta.")
        except FloatingPointError:
            print("Número não é flutuante.")
        except errors.IncorrectWhitespace:
            print("Uso incorreto de tabulação e/ou espaço em branco dentro do número.")
        except errors.IncorrectSymbol:
            print("Símbolo desconhecido ou não suportado usado.")
        except KeyboardInterrupt:
            print("Conversão interrompida.")
        except Exception as error:
            print(f"Erro não previsto: {error}, Tipo: {type(error)}")
        finally:
            backToInterface()

    elif (option == 10):
        clearTerminal()
        print("10. Formatação e largura fixa")

        try:
            print("> Qual operação?\n")
            print("1. to_fixed_width_bin")
            print("2. ipv4_to_bin")
            print("3. bin_to_ipv4")
            op : int = int(input("Operação: "))
            if (op == 1):
                num_fixed = (input("Num:  "))
                bits  = (input("Bits: "))
                print(to_fixed_width_bin(num_fixed, bits)) # type: ignore
            elif (op == 2):
                num_ipv4 = input("Ipv4: ")
                print(ipv4_to_bin(num_ipv4))
            elif (op == 3):
                num_bin : str = input("Binary Ipv4: ")
                print(bin_to_ipv4(num_bin))
            retry()
        except ValueError:
            print("Valor não é um numero válido.")
        except SyntaxError:
            print("Argumentos de tipo incorreto.")
        except KeyboardInterrupt:
            print("Conversão interrompida.")
        except Exception as error:
            print(f"Erro não previsto: {error}, Tipo: {type(error)}")
        finally:
            backToInterface()

    return None

def option2() -> None:
    clearTerminal()
    printLine()

    entry_text : str = '''
> Seja bem vindo(a) ao menu de testes automatizados!
> Por favor, escolha uma opção:
    
    0. Voltar ao menu principal
    1. Testes automatizados
    '''    
    
    print(entry_text)

    option : int = int()
    try:
        option : int = int(input("Digite sua escolha: "))
        if (option < 0) or (option > 1):
            raise(ValueError)
    except ValueError:
        print("Escolha inválida!\nVoltando ao menu principal...")
        sleep(timer)
        clearTerminal()
        interface()
    except KeyboardInterrupt:
        exit()
    except Exception as error:
        print(f"Erro não previsto: {error}, Tipo: {type(error)}")
        
    if (option == 0):
        print("\n> Voltando ao menu principal...")
        sleep(timer)
        clearTerminal()
        interface()
    elif (option == 1):
        clearTerminal()
        printLine()
        print("    1. Testes automatizados")
        printLine()
        main_test()
        printLine()

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

    option : int = int()
    try:
        option = int(input("Digite sua escolha: "))
        if (option < 1) or (option > 3):
            raise(ValueError)
    except ValueError:
        print("Escolha inválida!\nTerminando programa...")
        sleep(timer)
        clearTerminal()
        exit()
    except KeyboardInterrupt:
        exit()
    except Exception as error:
        print(f"Erro não previsto: {error}, Tipo: {type(error)}")

    if (option == 1):
        option1()
    elif (option == 2):
        option2()
    elif (option == 3):
        print("> Saindo...")
        sleep(timer)
        exit()
    
    return None

if __name__ == "__main__":
    interface()
