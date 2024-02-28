import socket
import threading


class Serveur:
    def __init__(self, hote, port):
        self.hote = hote
        self.port = port
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((self.hote, self.port))
        self.clients = []
        self.pseudos = []


    def diffusion(self, message):
        for client in self.clients:
            client.send(message)


    def gerer_client(self, client):
        while True:
            try:
                message = client.recv(1024)
                self.diffusion(message)
            except Exception as e:
                print(f"Erreur lors du traitement du client : {e}")
                index = self.clients.index(client)
                self.clients.remove(client)
                client.close()
                pseudo = self.pseudos[index]
                self.diffusion(f'{pseudo} a quitté la discussion'.encode('utf-8'))
                self.pseudos.remove(pseudo)
                break


    def recevoir_clients(self):
        while True:
            client, adresse = self.server_socket.accept()
            print(f"Connecté avec {str(adresse)}")
            client.send('pseudo'.encode('utf-8'))
            pseudo = client.recv(1024).decode('utf-8')
            self.pseudos.append(pseudo)
            self.clients.append(client)
            print(f"Le pseudo du client est {pseudo}")
            self.diffusion(f'{pseudo} a rejoint le chat'.encode('utf-8'))
            thread = threading.Thread(target=self.gerer_client, args=(client,))
            thread.start()

    def demarrer(self):
        print("Serveur en écoute")
        self.server_socket.bind((self.hote, self.port))
        self.server_socket.listen(5)
        self.recevoir_clients()