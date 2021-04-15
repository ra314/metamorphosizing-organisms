import socket
T_PORT = 12345
TCP_IP = '127.0.0.1'
BUF_SIZE = 30

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((TCP_IP, T_PORT))

sock.listen()
client1, addr1 = sock.accept()

while True :
    data = client1.recv(BUF_SIZE)
    client1.send("lol".encode())
