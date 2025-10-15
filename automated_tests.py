#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from exercicio01 import dec_to_bin
from exercicio02 import bin_to_dec
from exercicio03 import dec_to_oct
from exercicio04 import oct_to_dec
from exercicio05 import dec_to_hex
from exercicio06 import hex_to_dec
from exercicio07 import convert_base
from exercicio08 import decfrac_to_bin
from exercicio09 import binfrac_to_dec
from exercicio10 import bin_to_ipv4, ipv4_to_bin, to_fixed_width_bin

def test(test_input, expect_output, test_output) -> None:
    try:
        assert (test_output) == expect_output
        print(f"Passa: Converter {test_input} para {expect_output}.")
    except AssertionError:
        print(f"Falha: Converter {test_input} para {expect_output}")
    except Exception as error:
        print(f"Erro não previsto: {error}, Tipo: {type(error)}")
    return None

def test_exercicio01() -> None:
    print("\n*-- Exercício 01 - Decimal para Binário ---*")
    
    tests_ex_01 : dict[int, str] = {
        13 : "1101",
        0 : "0",
        -8 : "-1000",
    }

    for test_input, expect_output in tests_ex_01.items():
        test(test_input, expect_output, dec_to_bin(test_input))

    return None

def test_exercicio02() -> None:
    print("\n*--- Exercício 02 - Binário para decimal ---*")
        
    tests_ex_02 : dict[str, int] = {
        "1101" : 13,
        "-1000" : -8,
        "0" : 0,
    }
    
    for test_input, expect_output in tests_ex_02.items():
        test(test_input, expect_output, bin_to_dec(test_input))
    
    return None

def test_exercicio03() -> None:
    print("\n*--- Exercício 03 - Decimal para Octal ---*")
    
    tests_ex_03 : dict[int, str] = {
        93 : "135",
        -64 : "-100",
        0 : "0"
    }
    
    for test_input, expect_output in tests_ex_03.items():
        test(test_input, expect_output, dec_to_oct(test_input))
    
    return None

def test_exercicio04() -> None:
    print("\n*--- Exercício 04 - Octal para Decimal ---*")

    tests_ex_04 : dict[str, int] = {
        "135" : 93,
        "-3547" : -1895,
        "0" : 0
    }
    
    for test_input, expect_output in tests_ex_04.items():
        test(test_input, expect_output, oct_to_dec(test_input))

    return None

def test_exercicio05() -> None:
    print("\n*--- Exercício 05 - Decimal para Hexadecimal ---*")

    tests_ex_05 : dict[int, str] = {
        255 : "FF",
        -26 : "-1A",
        0 : "0"
    }

    for test_input, expect_output in tests_ex_05.items():
        test(test_input, expect_output, dec_to_hex(test_input))

    return None

def test_exercicio06() -> None:
    print("\n*--- Exercício 06 - Hexadecimal para Decimal ---*")

    tests_ex_06 : dict[str, int] = {
        "F66" : 3942,
        "-ccd" : -3277,
        "0" : 0
    }

    for test_input, expect_output in tests_ex_06.items():
        test(test_input, expect_output, hex_to_dec(test_input))

    return None

def test_exercicio07() -> None:
    print("\n*--- Exercício 07 - Conversão genérica de bases ---*")

    tests_ex_07 : dict[str, str] = {
        "1101" : "D",
        "-ZZZ" : "-46655",
        "0" : "0"
    }

    bases_ex_07 : dict[int, int] = {
        2 : 16,
        36 : 10,
        10 : 10
    }

    for (test_input, expect_output), (base_from, base_to) in zip(tests_ex_07.items(), bases_ex_07.items()):
        test(test_input, expect_output, convert_base(test_input, base_from, base_to))
        
        print(f"Da base {base_from} para {base_to}.")

    return None

def test_exercicio08() -> None:
    print("\n*--- Exercício 08 - Decimal fracionário para binário fracionário ---*")

    tests_ex_08 : dict[float, str] = {
        10.625 : "1010.101",
        0.1 : "0.0001100110",
        0 : "0"
    }

    frac_bits_ex_08 : list[int] = [8, 10, 1]

    for (test_input, expect_output), (frac_bits) in zip(tests_ex_08.items(), frac_bits_ex_08):
        test(test_input, expect_output, decfrac_to_bin(test_input, frac_bits))

        if (frac_bits == 1):
            print(f"Com {frac_bits} casa de precisão.")
        else:
            print(f"Com {frac_bits} casas de precisão.")

    return None

def test_exercicio09() -> None:
    print("\n*--- Exercício 09- Binário fracionário para decimal fracionário ---*")

    tests_ex_09 : dict[str, float] = {
        "0.01" : 0.25,
        "-1111001.1" : -121.5,
        "0.0" : 0.0
    }

    for test_input, expect_output in tests_ex_09.items():
        test(test_input, expect_output, binfrac_to_dec(test_input))

    return None

def test_exercicio10() -> None:
    print("\n*--- Exercício 10- Formatação e largura fixa ---*")
    
    print("\n1. Decimal para binário preenchido:")
    
    tests_ex_10_width : dict[int, str] = {
        5 : "00000101",
        22 : "0000000000010110",
        0 : "0000",
    }

    ex_10_width : list[int] = [8, 16, 4]

    for (test_input, expect_output), (width) in zip(tests_ex_10_width.items(), ex_10_width):
        test(test_input, expect_output, to_fixed_width_bin(test_input, width))

        if (width == 1):
            print(f"Com {width} casa de preenchimento.")
        else:
            print(f"Com {width} casas de preenchimento.")

    print("\n2. IPv4 para binário:")

    tests_ex_10_ipv4 : dict[str, str] = {
        "192.168.0.1" : "11000000.10101000.00000000.00000001",
        "111.222.4.6" : "01101111.11011110.00000100.00000110",
        "127.255.9.0" : "01111111.11111111.00001001.00000000"
    }

    for test_input, expect_output in tests_ex_10_ipv4.items():
        test(test_input, expect_output, ipv4_to_bin(test_input))

    print("\n3. Binário para IPv4")

    tests_ex_10_bin : dict[str, str] = {
        "00110101.11010000.11111111.00000000" : "53.208.255.0",
        "11101010.01100101.00000010.00000100" : "234.101.2.4",
        "01111000.01111000.00000001.00000101" : "120.120.1.5"
    }

    for test_input, expect_output in tests_ex_10_bin.items():
        test(test_input, expect_output, bin_to_ipv4(test_input))

    return None

def main_test() -> None:
    test_exercicio01()
    test_exercicio02()
    test_exercicio03()
    test_exercicio04()
    test_exercicio05()
    test_exercicio06()
    test_exercicio07()
    test_exercicio08()
    test_exercicio09()
    test_exercicio10()
    print()

    return None

if __name__ == "__main__":
    main_test()
