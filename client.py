import socket
import threading

class Client:
    def __init__(self, hote, port):
        self.hote = hote
        self.port = port
        self.pseudo = input("Rentrer un pseudo : ")
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect((self.hote, self.port))
def recevoir():
    while True:
        try:
            message = client.recv(1024).decode('utf-8')
            if message == 'pseudo':
                client.send(pseudo.encode('utf-8'))
            else:
                print(message)
        except:
            print("il ya une erreur")
            client.close()
            break


def write():
    while True:
        message = f'{pseudo}: {input("")}'
        client.send(message.encode('utf-8'))


receive_thread = threading.Thread(target=recevoir)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()
