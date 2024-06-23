from Interface import MessageWindow
from Connection import Connection



def start_client(ip, port):
    
    connection = Connection()

    isConnected = connection.start_connection(ip, port)
    print(f"Conectado ao servidor em {ip}:{port}\n")

    if(isConnected):
        window = MessageWindow()
        window.plotWindow()
        isConnected=False
    connection.end_connection()

if __name__ == "__main__":
    # Especifica o endereço IP e a porta do servidor
    IP = "127.0.0.1"
    PORT = 8080

    start_client(IP, PORT)
