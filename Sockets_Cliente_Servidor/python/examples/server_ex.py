import socket

# establecemos direccion

HOST = '127.0.0.1'  # La direccion de loopback
PUERTO = 65123  # puertos mayores a 1023 son libres / para escucha

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PUERTO))
    s.listen()
    conexion, direccion = s.accept()

    with conexion:
        print('conectado a:',direccion)

        while True:
            data = conexion.recv(1024)

            if not data:
                break

            conexion.send(data)
