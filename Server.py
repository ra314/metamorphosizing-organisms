import socket
def create_player(client):
	client.send("Send name")
	name = client.recv(BUF_SIZE)
	client.send("Pick organism")

#Setting up Socket
T_PORT = 12345
TCP_IP = '127.0.0.1'
BUF_SIZE = 4096
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((TCP_IP, T_PORT))

#Connecting to clients
sock.listen()
client1, addr1 = sock.accept()
client2, addr2 = sock.accept()

while True :
    data = client1.recv(BUF_SIZE)
    client1.send("lol".encode())
