import socket

class Connection():

    _instance = None

    def __init__(self):
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    @classmethod
    def instance(cls):
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance
        
    def start_connection(self, ip, port):  
        try:
            self.client_socket.connect((ip, port))
            return True
        except socket.error:
            return False
    def end_connection(self):
        self.client_socket.close()
    def send_message(self, message):
        self.client_socket.sendall(message)