import socket
import threading

pseudo = input('rentrer un pseudo')
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('10.10.95.178', 12345))

