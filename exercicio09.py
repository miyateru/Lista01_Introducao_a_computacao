def binfrac_to_dec(binary: str) -> float:
    

    return 

def main () -> None:
    try:
        num : str = input('> ')
        print(binfrac_to_dec(num))
    except Exception as error:
        print(f'Uncaught error: {error}, {type(error)}')

    return None

if __name__ == "__main__":
    main()
