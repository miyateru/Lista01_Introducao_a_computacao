import errors
from exercicio01 import dec_to_bin

def bin_to_ipv4(bits : str) -> str:
    return ""

def ipv4_to_bin(ip : str) -> str:
    blocks : list[str] = ip.split('.')
    result : str = str()
    
    for i in range(len(blocks)):
        block_bin : int =  int(dec_to_bin(int(blocks[i])))
        result += to_fixed_width_bin(block_bin, 8)
        if (i < len(blocks) - 1):
            result += '.'
            
    return result

def to_fixed_width_bin(n : int, bits : int) -> str:
    errors.in_base(str(n))
    errors.signal_placement(str(n))
    n = int(n)
    
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
        # num = int(input("Num:  "))
        # bits = int(input("Bits: "))
        # print(to_fixed_width_bin(num, bits))
        num = input("Ipv4: ")
        print(ipv4_to_bin(num))
    except Exception as error:
        print(f"Erro não previsto: {error}, Tipo: {type(error)}")
    return None
    
if __name__ == "__main__":
    _main()
