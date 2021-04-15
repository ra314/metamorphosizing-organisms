import socket
T_PORT = 12345
TCP_IP = '127.0.0.1'
BUF_SIZE = 30

k = socket.socket (socket.AF_INET, socket.SOCK_STREAM)
k.connect((TCP_IP, T_PORT))
MSG = "Hello karl"
k.send(MSG.encode())
