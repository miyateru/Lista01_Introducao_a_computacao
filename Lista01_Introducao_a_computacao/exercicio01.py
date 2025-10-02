def dec_to_bin(n: int) -> str:
    negative : bool = False
    result : str = ""

    if (n == 0):
        return str(0)
    
    if (n < 0):
        negative = True
        n = abs(n)
    
    while (n > 0):
        result += str(n % 2)
        n //= 2
    
    if (negative):
        result += '-'
    
    return result[::-1]

def main() -> None:
    try:
        num = int(input("> "))
        print(dec_to_bin(num))
    except Exception as error:
        print(f"Uncaught error: {error}", {type(error)})

    return None

if __name__ == "__main__":
    main()
