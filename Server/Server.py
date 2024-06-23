import socket
from cryptography.fernet import Fernet
from itertools import product


def generate_6t8b_table():
    # Gerar todas as combinações de 8 bits
    eight_bit_combinations = [format(i, '08b') for i in range(256)]
    
    # Gerar todas as combinações de 6 trits (0, 1, 2)
    six_trit_combinations = [''.join(map(str, comb)) for comb in product('012', repeat=6)]
    
    # Mapear as 256 primeiras combinações de 6 trits às combinações de 8 bits
    mapping_table = {six_trit_combinations[i]:eight_bit_combinations[i] for i in range(256)}
    
    return mapping_table

def ternary_to_binary(ternary_input, mapping_table):
    # Verifica se o comprimento do input binário é múltiplo de 8
    if len(ternary_input) % 6 != 0:
        raise ValueError("O comprimento da entrada binária deve ser múltiplo de 6.")

    binary_output = []

    # Divide a entrada binária em blocos de 8 bits e converte cada bloco
    for i in range(0, len(ternary_input), 6):
        byte = ternary_input[i:i+6]
        if byte in mapping_table:
            binary_output.append(mapping_table[byte])
        else:
            raise ValueError(f"Bloco de 6 ternarios não encontrado na tabela de mapeamento: {byte}")

    return ''.join(binary_output)


def binary_to_string(binary_input):
    # Verifica se o comprimento do input binário é múltiplo de 8
    if len(binary_input) % 8 != 0:
        raise ValueError("O comprimento da entrada binária deve ser múltiplo de 8.")
    
    # Lista para armazenar os caracteres convertidos
    chars = []

    # Divide a entrada binária em blocos de 8 bits e converte cada bloco
    for i in range(0, len(binary_input), 8):
        byte = binary_input[i:i+8]
        # Converte o bloco de 8 bits em um valor decimal
        decimal = int(byte, 2)
        # Converte o valor decimal em um caractere ASCII e adiciona à lista
        chars.append(chr(decimal))
    
    # Junta os caracteres em uma string e retorna
    return ''.join(chars)


def start_server(ip, port):

    # Cria um socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((ip, port))
    server_socket.listen(5)
    print(f"Servidor escutando em {ip}:{port}")

    #abre a chave de criptografia
    with open('chave.key', 'rb') as filekey:
        chave = filekey.read()
    fernet = Fernet(chave)

    #cria tabela
    table = generate_6t8b_table()

    while True:
        # Aceita uma conexão de um cliente
        client_socket, client_address = server_socket.accept()
        print(f"Conexão aceita de {client_address}\n")

        while True:
            # Recebe mensagem do cliente
            ternary_message = client_socket.recv(1024).decode('utf-8')
            binary_message = ternary_to_binary(ternary_message, table)
            encrtpted_message = binary_to_string(binary_message).encode()
            message = fernet.decrypt(encrtpted_message).decode()
            

            print(f"Mensagem recebida ternaria: {ternary_message}\n")
            print(f"Mensagem recebida binaria: {binary_message}\n")
            print(f"Mensagem recebida encriptada: {encrtpted_message}\n")
            print(f"Mensagem recebida: {message}\n")            



if __name__ == "__main__":

    IP = "127.0.0.1"
    PORT = 8080

    start_server(IP, PORT)
