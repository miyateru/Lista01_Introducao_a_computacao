def decfrac_to_bin(num: float, max_frac_bits: int = 16) -> str:

    return "depressao"

def main () -> None:
    num : float = float(input("Número a ser convertido: "))
    max_frac : int = int(input("Precisão da parte fracionária: "))

    print(decfrac_to_bin(num, max_frac))

    return None

if __name__ == "__main__":
    main()
    