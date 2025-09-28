
def oct_to_dec(b: str) -> int:
    decimal : int = 0
    negativo : bool = False

    characteresValidos : list[str] = ['0', '1', '2', '3', '4', '5', '6', '7', '-']

    if ("-" in b) and (0 != b.index("-")):
        raise ValueError
    
    for N in range(len(b)):
        if b[N] not in characteresValidos:
            raise TypeError

    if "-" in b:
        negativo = True
        b = b.replace("-", "")

    b = b[::-1]
    
    for N in range(len(b)):
        decimal += int(b[N]) * (8 ** N)
    
    if negativo:
        decimal *= (-1)

    return decimal

def main () -> None:
    num = input(" > ")
    
    print(oct_to_dec(num))

    return None

if __name__ == "__main__":
    main()
