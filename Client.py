import os
#Communicating with server
def communicate():
	#Parsing server info
	data = sock.recv(BUF_SIZE).decode('utf-8')
	data_buffer = data.split("ENDENDEND")
	
	#Going through the buffer
	while data_buffer:
		#Clearing previous print
		os.system('cls' if os.name == 'nt' else 'clear')
		#Printing latest part of data buffer
		data = data_buffer.pop(0)
		print(data, end = "")
		
		if data == "Session Over":
			return 0
		
		#Sending back a message, if the input isn't empty
		message = input()
		if message:
			sock.send(message.encode())
			
	return 1

from PrepareSocket import *
#Connecting to server		
sock.connect((TCP_IP, T_PORT))		
while communicate():
	pass
