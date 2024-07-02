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
                # #Input de entrada
                # message = input(f"Digite a mensagem para enviar ao servidor (ou 'exit' para sair):\n ")
                # #Processamentos da mensagem
                # crypto_message = fernet.encrypt(message.encode('UTF-8'))
                # binary_message = Alg.string_to_binary(crypto_message)
                # message_6t = Alg.binary_to_ternary(binary_message, map8b6t)
                # #Saída dos processamentos
                # print(f"Mensagem enviada: {message}\n")
                # print(f"Mensagem enviada criptografada: {crypto_message}\n")
                # print(f"Mensagem enviada em binário: {binary_message}\n")
                # print(f"Mensagem enviada em ternário: {message_6t}\n")

                # Alg.plot_signal(message_6t)

                # #Envio da mensagem
                # connection.send_message(message_6t.encode())

            #-----------------------------------------SEM CRIPTOGRAFIA------------------------------------------------


                #Input de entrada
                message = input(f"Digite a mensagem para enviar ao servidor (ou 'exit' para sair):\n ")
                #Processamentos da mensagem
                binary_message = message

                message_6t = pattern_to_pattern(binary_message)

                #balanço DC
                positive = message_6t.count('+')
                negative = message_6t.count('-')
                saldo = positive - negative
                tamanho_bloco = 6
                if ((saldo) >= 2 or (saldo) <= -2):
                    j = 0
                    balanco = 0
                    for i in range(0, len(message_6t), tamanho_bloco):
                        bloco = message_6t[i:i + tamanho_bloco]
                        quantidade_mais = bloco.count('+')
                        quantidade_menos = bloco.count('-')
                        balanco[j] = quantidade_mais - quantidade_menos
                        j = j+1
                    j = j-1
                    while (saldo >= 2):
                        if(balanco[j] == 1):
                            for i in range(j*6, j*6+6, 1):
                                if (message_6t[i] == '+'):
                                    message_6t[i] = '-'
                                elif (message_6t[i] == '-'):
                                    message_6t[i] = '+'
                            saldo =  saldo - 2
                        j = j-1
                        
                        



                                           
                #Saída dos processamentos
                print(f"Mensagem enviada: {message}\n")
                print(f"Mensagem enviada em binário: {binary_message}\n")
                print(f"Mensagem enviada em ternário: {message_6t}\n")

                Alg.plot_signal(message_6t)

                #Envio da mensagem
                connection.send_message(message_6t.encode())


        except KeyboardInterrupt:

            print("\nConexão encerrada pelo usuário.")

        finally:
            # Fecha o socket do cliente
            connection.end_connection()


if __name__ == "__main__":
    # Especifica o endereço IP e a porta do servidor
    IP = "192.168.100.74"
    PORT = 8080

    start_client(IP, PORT)
