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
            message_8b = []
            for i in range(len(message_6t)//6):
                value=map6t8b[message_6t[6*i:6*i+6]]
                decimal_value= int(value, 2)
                byte_value = decimal_value.to_bytes(1, byteorder='big')
                message_8b.append(byte_value)
            
            final_bytes = b''.join(message_8b)

            # Recebe mensagem do cliente
            encrypeted_message = final_bytes.decode('UTF-8')

            decrypt_message = fernet.decrypt(encrypeted_message.encode('UTF-8')).decode('utf-8')
            #message = binary_to_string(decrypt_message)
                

            print(f"Mensagem recebida criptografa: {encrypeted_message}\n")
            print(f"Mensagem recebida descriptografa: {decrypt_message}\n")
            #print(f"Mensagem recebida: {message}\n")



        client_socket.close()

if __name__ == "__main__":

    IP = "127.0.0.1"
    PORT = 8080

    start_server(IP, PORT)
