from prepare_socket import *
import os

#Connecting to server
sock.connect((TCP_IP, T_PORT))

#Communicating with server
while True:
	os.system('cls' if os.name == 'nt' else 'clear')
	data = sock.recv(BUF_SIZE).decode('utf-8')
	print(data, end = '')
	message = input()
	sock.send(message.encode())
