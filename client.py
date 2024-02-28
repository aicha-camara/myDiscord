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

    def write(self):
        while True:
            message = f'{self.pseudo}: {input("")}'
            self.client.send(message.encode('utf-8'))

if __name__ == "__main__":
    hote = '10.10.97.162'
    port = 55555
    client = Client(hote, port)

    receive_thread = threading.Thread(target=client.recevoir)
    receive_thread.start()

    write_thread = threading.Thread(target=client.write)
    write_thread.start()