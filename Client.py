import os

# Responding to the server
def respond():
	# Sending back a message, if the input isn't empty
	message = input()
	if message:
		sock.send(message.encode())

# Listening to the server
def communicate():
	# Parsing server info
	data = sock.recv(BUF_SIZE).decode('utf-8')
	
	# Parsing data buffer
	if "ENDENDEND" in data:
		data_buffer = data.split("ENDENDEND")
		# Going through the buffer
		while data_buffer:
			# Retrieving latest part of buffer
			data = data_buffer.pop(0)
			# Clearing previous print
			os.system('cls' if os.name == 'nt' else 'clear')
			print(data, end="")

			# Ending session
			if data == "Session Over.\n":
				return 0
		
			respond()
	else:
		print(data, end="")
		respond()

	return 1


from PrepareSocket import *

# Connecting to server
sock.connect((TCP_IP, T_PORT))
while communicate():
	pass
