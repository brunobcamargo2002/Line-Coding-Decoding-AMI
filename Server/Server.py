import socket
from cryptography.fernet import Fernet

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

    while True:
        # Aceita uma conexão de um cliente
        client_socket, client_address = server_socket.accept()
        print(f"Conexão aceita de {client_address}\n")

        while True:
            # Recebe mensagem do cliente
            print("teste")
            encrypeted_message = client_socket.recv(1024).decode('utf-8')
            print("teste")
            decrypt_message = fernet.decrypt(encrypeted_message).decode('utf-8')
            message = binary_to_string(decrypt_message)
            

            print(f"Mensagem recebida criptografa: {encrypeted_message}\n")
            print(f"Mensagem recebida descriptografa: {decrypt_message}\n")
            print(f"Mensagem recebida: {message}\n")



        client_socket.close()

if __name__ == "__main__":

    IP = "127.0.0.1"
    PORT = 8080

    start_server(IP, PORT)
