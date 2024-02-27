import socket
import threading

pseudo = input('rentrer un pseudo')
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('10.10.95.178', 12345))

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

