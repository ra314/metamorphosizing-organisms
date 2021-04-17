from prepare_socket import *

#Connecting to server
sock.connect((TCP_IP, T_PORT))

#Communicating with server
while True:
	data = sock.recv(BUF_SIZE).decode('utf-8')
	print(data, end = '')
	message = input()
	sock.send(message.encode())
