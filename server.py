import socket

host = '192.168.1.166'
port = 12345

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server_socket.listen(5)

clients = []
pseudo = []

def broadcast(message):
    for client in clients:
        client.send(message)

def handle(client):
    while True:
        try:
            message = client.recv(1024)
            broadcast(message)
        except:
            index = clients.index(client)
            clients.remove(client)
            client.close()
            pseudo = pseudo[index]
            broadcast(f'{pseudo} a quitter la discussion'.encode('ascii'))
            pseudo.remove(pseudo)
            break
