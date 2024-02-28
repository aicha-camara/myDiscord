import socket
import threading


class Client:
    def __init__(self, hote, port):
        self.hote = hote
        self.port = port
        self.pseudo = input("Rentrer un pseudo : ")
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect((self.hote, self.port))

    def recevoir(self):
        while True:
            try:
                message = self.client.recv(1024).decode('utf-8')
                if message == 'pseudo':
                    self.client.send(self.pseudo.encode('utf-8'))
                else:
                    print(message)
            except Exception as e:
                print(f"Il y a une erreur : {e}")
                self.client.close()
                break


def write():
    while True:
        message = f'{pseudo}: {input("")}'
        client.send(message.encode('utf-8'))


receive_thread = threading.Thread(target=recevoir)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()
