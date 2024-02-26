import socket
from signal import signal, SIGPIPE, SIG_DFL  

client = True
server = False
port = 8008
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect(("127.0.0.1", port))
while True:
	data = s.recv(1024)
	print(data.decode())
	s.send(input("Please write your message: ").encode())
        
        
