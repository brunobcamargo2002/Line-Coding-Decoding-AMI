from itertools import product
from itertools import product

def generate_8b6t_table():
    # Gerar todas as combinações de 8 bits
    eight_bit_combinations = [format(i, '08b') for i in range(256)]
    
    # Gerar todas as combinações de 6 trits (0, 1, 2)
    six_trit_combinations = [''.join(map(str, comb)) for comb in product('012', repeat=6)]
    
    # Mapear as 256 primeiras combinações de 6 trits às combinações de 8 bits
    mapping_table = {eight_bit_combinations[i]: six_trit_combinations[i] for i in range(256)}
    
    return mapping_table

def binary_to_ternary(binary_input, mapping_table):
    # Verifica se o comprimento do input binário é múltiplo de 8
    if len(binary_input) % 8 != 0:
        raise ValueError("O comprimento da entrada binária deve ser múltiplo de 8.")

    ternary_output = []

    # Divide a entrada binária em blocos de 8 bits e converte cada bloco
    for i in range(0, len(binary_input), 8):
        byte = binary_input[i:i+8]
        if byte in mapping_table:
            ternary_output.append(mapping_table[byte])
        else:
            raise ValueError(f"Bloco de 8 bits não encontrado na tabela de mapeamento: {byte}")

    return ''.join(ternary_output)

def string_to_binary(message):
    binary_representation = ''.join(format(ord(char), '08b') for char in message)
    return binary_representation