import socket

HOST = '127.0.0.1'  # IP del servidor no del cliente
PUERTO = 65123  # Puerto de envio

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PUERTO))

    s.sendall(b'Hola mundo')

    data = s.recv(1024)

print('recibido', repr(data))
