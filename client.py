import socket
import threading

pseudo = input("rentrer un pseudo")
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('10.10.97.162', 55555))


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
