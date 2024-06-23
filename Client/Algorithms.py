from matplotlib import pyplot as plt
from scipy import signal
import numpy as np

from itertools import product
from itertools import product

#Plot do Gráfico
def plot_signal(signal):

    pontos_por_signal=100
    time_step=0.01

    signal_value = []
    for s in signal:
        if(s=='+'):
            signal_value.append(1)
        elif(s=='0'):
            signal_value.append(0)
        else:
            signal_value.append(-1)
    
    axisX = np.arange(0, (pontos_por_signal*time_step*len(signal_value)), time_step)
    axisY = np.zeros(axisX.size)

    count = 0
    for i in range(axisX.size):
        axisY[i]=signal_value[count]
        if((i+1)%pontos_por_signal==0):
            count+=1

    plt.plot(axisX, axisY)
    plt.show()

def generate_8b6t_table():
    # Gerar todas as combinações de 8 bits
    eight_bit_combinations = [format(i, '08b') for i in range(256)]
    
    # Gerar todas as combinações de 6 trits (0, 1, 2)
    six_trit_combinations = [''.join(map(str, comb)) for comb in product('-0+', repeat=6)]
    
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

#Converte uma string para byte
def string_to_binary(crypto_message):
    binary_representation = ''.join(format(byte, '08b') for byte in crypto_message)
    return binary_representation


