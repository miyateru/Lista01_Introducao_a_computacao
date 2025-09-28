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
        resultado += str(n % 8)
        n //= 8
    
    if (negativo):
        resultado += '-'
    
    return resultado[::-1]

def main() -> None:
    num = int(input("> "))
    print(dec_to_bin(num))

    return None

if __name__ == "__main__":
    main()
