import socket
import threading

hote = '10.10.95.178'
port = 12345

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((hote, port))
server_socket.listen(5)

clients = []
pseudos = []


def diffusion(message):
    for client in clients:
        client.send(message)


def gerer(client):
    while True:
        try:
            message = client.recv(1024)
            diffusion(message)
        except:
            index = clients.index(client)
            clients.remove(client)
            client.close()
            pseudo = pseudos[index]
            diffusion(f'{pseudo} a quitté la discussion'.encode('utf-8'))
            pseudos.remove(pseudo)
            break


def recevoir():
    while True:
        client, adresse = server_socket.accept()
        print(f"connecté avec {str(adresse)}")
        client.send('pseudo'.encode('utf-8'))
        pseudo = client.recv(1024).decode('utf-8')
        pseudos.append(pseudo)
        clients.append(client)
        print(f"Le pseudo du client est {pseudo}")
        diffusion(f'{pseudo} a rejoint le chat'.encode('utf-8'))
        thread = threading.Thread(target=gerer, args=(client,))
        thread.start()


print("serveur en écoute")
recevoir()
