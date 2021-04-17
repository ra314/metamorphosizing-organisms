import socket
T_PORT = 12345
TCP_IP = '127.0.0.1'
BUF_SIZE = 4096

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Ensuring the socket is closed
import atexit
def close_socket():
	print("Socket closed.")
	sock.close()

atexit.register(close_socket)
