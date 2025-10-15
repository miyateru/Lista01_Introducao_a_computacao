import errors
from exercicio01 import dec_to_bin
from exercicio02 import bin_to_dec

def bin_to_ipv4(bits : str) -> str:
    blocks : list[str] = bits.split('.')
    result : str = str()
    
    for i in range(len(blocks)):
        result += str(bin_to_dec(blocks[i]))
        if (i < len(blocks) - 1):
            result += '.'
            
    return result

def ipv4_to_bin(ip : str) -> str:
    blocks : list[str] = ip.split('.')
    result : str = str()
    
    for i in range(len(blocks)):
        result += to_fixed_width_bin(int(blocks[i]), 8)
        if (i < len(blocks) - 1):
            result += '.'
            
    return result

def to_fixed_width_bin(n : int, bits : int) -> str:
    errors.in_base(str(n))
    errors.signal_placement(str(n))
    if (str(bits).isnumeric()) == False:
        raise SyntaxError("A base deve ser um número.")
    bits = int(bits)
    
    n = int(n)
    bits = int(bits)
    
    binary : str = dec_to_bin(n)
    result : str = str()
    
    negative : bool = False
    if ('-' in binary):
        negative = True
        binary = binary.replace('-', '')
    
    result : str = str()
    binary = binary[::-1]
    for i in range(bits, 0, -1):
        if (i <= len(binary)):
            result += binary[i - 1]
        else:
            result += '0'
    
    if (negative):
        result = result[::-1]
        result += '-'
        result = result[::-1]
    
    return result

def _main() -> None:
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
    except ValueError:
        print("Valor não é um numero válido.")
    except SyntaxError:
        print("Argumentos de tipo incorreto.")
    except KeyboardInterrupt:
        exit()
    except Exception as error:
        print(f"Erro não previsto: {error}, Tipo: {type(error)}")
    return None

if __name__ == "__main__":
    _main()
