from Connection import Connection
import Algorithms as Alg

from cryptography.fernet import Fernet
from itertools import product
from itertools import product

def start_client(ip, port):
    with open('chave.key', 'rb') as filekey:
        chave = filekey.read()
    fernet = Fernet(chave)
    # Cria um socket
    connection = Connection()

    # Conecta ao servidor
    connection.start_connection(ip, port)
    print(f"Conectado ao servidor em {ip}:{port}\n")

    #Gera Map 8b6t
    map8b6t = Alg.generate_8b6t_table()

    try:
        while True:
            # Recebe entrada do usuário
            
            message = input(f"Digite a mensagem para enviar ao servidor (ou 'exit' para sair):\n ")
            crypto_message = fernet.encrypt(message.encode('UTF-8'))
            binary_message = Alg.string_to_binary(crypto_message)
            message_6t= ""
            for i in range(len(binary_message)//8):
                message_6t+=map8b6t[binary_message[8*i:8*i+8]]

            print(f"Mensagem enviada: {message}\n")
            print(f"Mensagem enviada criptografada: {crypto_message}\n")
            print(f"Mensagem enviada em binário: {binary_message}\n")
            print(f"Mensagem com o código: {message_6t}\n")
            # Envia a mensagem ao servidor+
            connection.send_message(message_6t.encode())


    except KeyboardInterrupt:

        print("\nConexão encerrada pelo usuário.")

    finally:
        # Fecha o socket do cliente
        connection.end_connection()

if __name__ == "__main__":
    # Especifica o endereço IP e a porta do servidor
    IP = "127.0.0.1"
    PORT = 8080

    start_client(IP, PORT)
