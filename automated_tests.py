#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from exercicio01 import dec_to_bin
from exercicio02 import bin_to_dec
from exercicio03 import dec_to_oct
from exercicio04 import oct_to_dec
from exercicio05 import dec_to_hex
from exercicio06 import hex_to_dec
from exercicio07 import convert_base

def test(test_input, expect_output) -> None:
    try:
        assert (test_input) == expect_output
        print(f"Passa: Converter {test_input} para {expect_output}.")
    except AssertionError:
        print(f"Falha: Converter {test_input} para {expect_output}")
    except Exception as error:
        print(f"Erro não previsto: {error}, Tipo: {type(error)}")
    return None

def test_exercicio01() -> None:
    print("\n*-- Exercicio 01 - Decimal pra Binário --*")
    
    tests_ex_01 : dict[int, str] = {
        13 : "1101",
        0 : "0",
        -8 : "-1000",
    }
    
    for test_input, expect_output in tests_ex_01.items():
        test(dec_to_bin(test_input), expect_output)
    
    return None

def test_exercicio02() -> None:
    print("\n*--- Exercicio 02 - Binário pra decimal --*")
        
    tests_ex_02 : dict[str, int] = {
        "1101" : 13,
        "-1000" : -8,
        "0" : 0,
    }
    
    for test_input, expect_output in tests_ex_02.items():
        test(bin_to_dec(test_input), expect_output)
    
    return None

def test_exercicio03() -> None:
    print("\n*--- Exercicio 03 - Decimal pra Octal --*")
    
    tests_ex_03 : dict[int, str] = {
        93 : "135",
        -64 : "-100",
        0 : "0"
    }
    
    for test_input, expect_output in tests_ex_03.items():
        test(dec_to_oct(test_input), expect_output)
    
    return None

def test_exercicio04() -> None:
    return None

def test_exercicio05() -> None:
    return None

def test_exercicio06() -> None:
    return None

def test_exercicio07() -> None:
    return None

def test_exercicio08() -> None:
    return None

def test_exercicio09() -> None:
    return None

def test_exercicio10() -> None:
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
