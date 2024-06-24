import socket
import Algorithms as Alg
from cryptography.fernet import Fernet


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

    #Gera Map 8b6t
    map6t8b = Alg.generate_6t8b_table()

    while True:
        # Aceita uma conexão de um cliente
        client_socket, client_address = server_socket.accept()
        print(f"Conexão aceita de {client_address}\n")

        while True:
            message_6t= client_socket.recv(1024).decode()
            final_bytes = Alg.ternary_to_binary(message_6t, map6t8b)

            # Mensagem Criptografada
            encrypted_message = Alg.binary_to_string(final_bytes)
            # Mensagem Decriptografada
            decrypt_message = fernet.decrypt(encrypted_message.encode('UTF-8')).decode('utf-8')

            #Saída dos processamentos
            print(f"Mensagem recebida em ternário: {message_6t}\n")
            print(f"Mensagem recebida em binário: {final_bytes}\n")
            print(f"Mensagem recebida criptografada: {encrypted_message}\n")
            print(f"Mensagem recebida: {decrypt_message}\n")
            Alg.plot_signal(message_6t)

            #print(f"Mensagem recebida: {message}\n")
            if(decrypt_message=="exit"):
                break

        client_socket.close()

if __name__ == "__main__":

    IP = "127.0.0.1"
    PORT = 8080

    start_server(IP, PORT)
