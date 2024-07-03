import Algorithms as Alg
import teste4 as algoritmo
from cryptography.fernet import Fernet

from Connection import Connection

def start_client(ip, port):
    #Carrega a chave
    with open('chave.key', 'rb') as filekey:
        chave = filekey.read()
    fernet = Fernet(chave)

    # Cria um socket
    connection = Connection()

    # Conecta ao servidor
    isConnected = connection.start_connection(ip, port)

    #Gera Map 8b6t
    pattern_to_pattern, pattern_to_binary = algoritmo.generate_pattern_functions()

    if(isConnected):
        print(f"Conectado ao servidor em {ip}:{port}\n")
        try:
            while True:
                #Input de entrada
                message = input(f"Digite a mensagem para enviar ao servidor (ou 'exit' para sair):\n ")
                #Processamentos da mensagem
                crypto_message = fernet.encrypt(message.encode('UTF-8'))
                binary_message = Alg.string_to_binary(crypto_message)
                message_6t, bal = algoritmo.encode_octets_to_patterns(binary_message)
                #Saída dos processamentos
                print(f"Mensagem enviada: {message}\n")
                print(f"Mensagem enviada criptografada: {crypto_message}\n")
                print(f"Mensagem enviada em binário: {binary_message}\n")
                print(f"Mensagem enviada em ternário: {message_6t}\n")

                Alg.plot_signal(message_6t)

                #Envio da mensagem
                connection.send_message(message_6t.encode())

            #-----------------------------------------SEM CRIPTOGRAFIA------------------------------------------------


                # #Input de entrada
                # message = input(f"Digite a mensagem para enviar ao servidor (ou 'exit' para sair):\n ")
                # #Processamentos da mensagem
                # binary_message = message

                # message_6t, bal = algoritmo.encode_octets_to_patterns(binary_message)                
                        
                # #Saída dos processamentos
                # print(f"Binário da mensagem: {binary_message}\n")
                # print(f"Mensagem enviada em ternário: {bal}\n")

                # Alg.plot_signal(bal)

                # #Envio da mensagem
                # connection.send_message(bal.encode())


        except KeyboardInterrupt:

            print("\nConexão encerrada pelo usuário.")

        finally:
            # Fecha o socket do cliente
            connection.end_connection()


if __name__ == "__main__":
    # Especifica o endereço IP e a porta do servidor
    IP = "192.168.100.74"
    PORT = 8081

    start_client(IP, PORT)
