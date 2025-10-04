def dec_to_hex(n: int) -> str:
    char_table : dict[int, str] = {
        0 : '0',
        1 : '1',
        2 : '2',
        3 : '3',
        4 : '4',
        5 : '5',
        6 : '6',
        7 : '7',
        8 : '8',
        9 : '9',
        10 : 'A',
        11 : 'B',
        12 : 'C',
        13 : 'D',
        14 : 'E',
        15 : 'F',
    }
    result : str = ""
    
    if (n == 0):
        return str(0)

    negative : bool = False
    if n < 0:
        negative = True
        n = abs(n)
    
    while (n > 0):
        num : int = n % 16
        result += char_table[num]
        n //= 16
    
    if (negative):
        result += '-'
    
    return result[::-1]

def main() -> None:
    try:
        num = int(input("> "))
        print(dec_to_hex(num))
    except Exception as error:
        print(f"Uncaught error: {error}, {type(error)}")

    return None

if __name__ == "__main__":
    main()
