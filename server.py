import socket

# Créer un socket TCP/IP
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Liaison du socket à une adresse et un port
server_address = ('192.168.1.166', 12345)
server_socket.bind(server_address)

# Écouter les connexions entrantes
server_socket.listen(5)

while True:
    # Attendre une connexion
    print("En attente de connexion...")
    client_socket, client_address = server_socket.accept()
    print(f"Connexion depuis {client_address}")

    # Traiter les données entrantes
    while True:
        data = client_socket.recv(1024)
        if not data:
            break
        print(f"Reçu : {data.decode()}")
        client_socket.sendall(data)

    # Fermer la connexion
    client_socket.close()
