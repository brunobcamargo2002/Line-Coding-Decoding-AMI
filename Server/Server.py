import socket


def start_server(ip, port):
    # Cria um socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Vincula o socket ao endereço IP e porta especificados
    server_socket.bind((ip, port))

    # Coloca o socket em modo de escuta
    server_socket.listen(5)
    print(f"Servidor escutando em {ip}:{port}")

    while True:
        # Aceita uma conexão de um cliente
        client_socket, client_address = server_socket.accept()
        print(f"Conexão aceita de {client_address}")

        while True:
            # Recebe mensagem do cliente
            message = client_socket.recv(1024).decode('utf-8')
            if not message:
                # Se a mensagem estiver vazia, o cliente fechou a conexão
                print("Conexão encerrada pelo cliente")
                break

            # Imprime a mensagem recebida
            print(f"Mensagem recebida: {message}")

        # Fecha a conexão com o cliente
        client_socket.close()

if __name__ == "__main__":
    # Especifica o endereço IP e a porta
    IP = "127.0.0.1"
    PORT = 8080

    start_server(IP, PORT)
