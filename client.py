import socket
import threading

class ClientSocket:
    def __init__(self, hote="10.10.103.118", port=55556):
        self.hote = hote
        self.port = port
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect((self.hote, self.port))

    def recevoir(self, pseudo):
        while True:
            try:
                message = self.client.recv(1024).decode('utf-8')
                if message == 'pseudo':
                    self.client.send(pseudo.encode('utf-8'))
                else:
                    print(message)
            except Exception as e:
                print(f"Il y a une erreur : {e}")
                self.client.close()
                break

    def write(self, pseudo):
        while True:
            message = f'{pseudo}: {input("")}'
            self.client.send(message.encode('utf-8'))

if __name__ == "__main__":
    pseudo = input("Rentrer un pseudo : ")
    client_socket = ClientSocket()
    receive_thread = threading.Thread(target=client_socket.recevoir, args=(pseudo,))
    receive_thread.start()
    write_thread = threading.Thread(target=client_socket.write, args=(pseudo,))
    write_thread.start()
