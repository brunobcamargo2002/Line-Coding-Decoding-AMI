import socket
from cryptography.fernet import Fernet

def string_to_binary(message):
    binary_representation = ''.join(format(ord(char), '08b') for char in message)
    return binary_representation

def start_client(ip, port):

    with open('chave.key', 'rb') as filekey:
        chave = filekey.read()
    fernet = Fernet(chave)
    
    # Cria um socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Conecta ao servidor
    client_socket.connect((ip, port))
    print(f"Conectado ao servidor em {ip}:{port}")

    try:
        while True:
            # Recebe entrada do usuário
            
            message = input("Digite a mensagem para enviar ao servidor (ou 'exit' para sair): ")

            binary_message = string_to_binary(message)
            binary_encoded = binary_message.encode('utf-8')

            crypto_message = fernet.encrypt(binary_encoded)

            print(f"Mensagem enviada: {message}")
            print(f"Mensagem enviada em binário: {binary_message}")


            # Envia a mensagem ao servidor
            client_socket.sendall(crypto_message)


    except KeyboardInterrupt:
        print("\nConexão encerrada pelo usuário.")

    finally:
        # Fecha o socket do cliente
        client_socket.close()

if __name__ == "__main__":
    # Especifica o endereço IP e a porta do servidor
    IP = "127.0.0.1"
    PORT = 8080

    start_client(IP, PORT)
