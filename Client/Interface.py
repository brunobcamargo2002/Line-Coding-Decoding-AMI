import tkinter as tk
from Connection import Connection
import Algorithms
from Encrypter import Encrypter

class MessageWindow():
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Client-Side")
        self.window.geometry("600x400")  # Definindo o tamanho da janela

        # Estilo para fontes e cores
        font_label = ("Helvetica", 14)
        font_text = ("Helvetica", 12)
        font_button = ("Helvetica", 12)
        bg_color = "#333333"  # Cor de fundo escura para melhor contraste
        fg_color = "white"  # Cor do texto

        # Configuração do grid na janela principal
        self.window.grid_rowconfigure(0, weight=1)
        self.window.grid_columnconfigure(0, weight=1)

        # Frame para o rótulo "Message" e o widget de texto
        self.message_frame = tk.Frame(self.window, bg=bg_color)
        self.message_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        self.label = tk.Label(self.message_frame, text="Message", font=font_label, bg=bg_color, fg=fg_color)
        self.label.grid(row=0, column=0, padx=10, pady=10, sticky="w")

        self.text = tk.Text(self.message_frame, height=10, width=50, wrap=tk.WORD, font=font_text, bg=bg_color, fg=fg_color)
        self.text.grid(row=1, column=0, padx=10, pady=5, sticky="nsew")

        # Frame para o campo de entrada e botão "Send"
        self.entry_frame = tk.Frame(self.window, bg=bg_color)
        self.entry_frame.grid(row=1, column=0, padx=10, pady=10, sticky="ew")

        # Configuração para que o Entry ocupe todo o espaço disponível
        self.entry_frame.grid_columnconfigure(0, weight=1)

        self.entry = tk.Entry(self.entry_frame, font=font_text, bg=bg_color, fg=fg_color)
        self.entry.grid(row=0, column=0, padx=5, pady=10, sticky="ew")

        self.send_button = tk.Button(self.entry_frame, text="Send", width=10, font=font_button, command=self.printText, bg="#007ACC", fg="white")
        self.send_button.grid(row=0, column=1, padx=5, pady=10)

        # Ajuste para que os elementos se expandam conforme a janela é redimensionada
        self.message_frame.grid_rowconfigure(1, weight=1)
        self.message_frame.grid_columnconfigure(0, weight=1)
    def printText(self):
        connection = Connection()
        message = self.entry.get().strip()
        if len(message)>0:
            self.text.config(state=tk.NORMAL)
            self.text.insert(tk.END, message + "\n")
            self.text.config(state=tk.DISABLED)
            binary_message = Algorithms.string_to_binary(message)
            encrypter = Encrypter()
            cripto_message = encrypter.encrypt(binary_message)

            print(f"Mensagem enviada: {message}\n")
            print(f"Mensagem enviada em binário: {binary_message}\n")
            print(f"Mensagem enviada criptografada: {cripto_message}\n")


            connection.send_message(cripto_message)
        self.entry.delete(0, tk.END)
    def plotWindow(self):
        self.window.mainloop()