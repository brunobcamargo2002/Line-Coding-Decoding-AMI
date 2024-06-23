from cryptography.fernet import Fernet

class Encrypter:
    _instance = None

    def __init__(self):
        with open('chave.key', 'rb') as filekey:
            chave = filekey.read()
        self.fernet = Fernet(chave)

    @classmethod
    def instance(cls):
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance

    def encrypt(self, binaryMessage):
        crypto_message = self.fernet.encrypt(binaryMessage.encode('utf-8'))
        return crypto_message
