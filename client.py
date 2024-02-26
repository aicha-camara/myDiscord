import socket
import tkinter as tk

def send_message():
    message = message_entry.get()
    if message:
        client_socket.sendall(message.encode())
        received_data = client_socket.recv(1024)
        chat_text.insert(tk.END, f"Server: {received_data.decode()}\n")

def on_closing():
    client_socket.close()
    root.destroy()

# Créer une fenêtre
root = tk.Tk()
root.title("Chat Client")

# Créer une zone de chat
chat_text = tk.Text(root)
chat_text.pack()

# Créer une entrée pour les messages
message_entry = tk.Entry(root)
message_entry.pack()

# Créer un bouton d'envoi
send_button = tk.Button(root, text="Send", command=send_message)
send_button.pack()

# Configuration de la connexion au serveur
server_address = ('192.168.1.166', 12345)
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(server_address)

# Gestion de la fermeture de la fenêtre
root.protocol("WM_DELETE_WINDOW", on_closing)

# Lancement de la boucle principale
root.mainloop()
