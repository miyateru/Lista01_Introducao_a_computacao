#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def bin_to_dec(b: str) -> int:
    decimal : int = 0
    negativo : bool = False

    if ('-' in b) and (0 != b.index('-')):
        raise ValueError

    if '-' in b:
        negativo = True
        b = b.replace('-', "")

    b = b[::-1]
    
    for N in range(len(b)):
        decimal += int(b[N]) * (2 ** N)
    
    if negativo:
        decimal *= (-1)

    return decimal

def main () -> None:
    num = input(" > ")
    
    print(bin_to_dec(num))

    return None

if __name__ == "__main__":
    main()
