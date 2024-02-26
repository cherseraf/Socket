import socket

client = False
server = True
port = 8008
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

if server:
    s.bind(("127.0.0.1", port))
    s.listen()
    
    while True:
        connect, addr = s.accept()
        connect.send(b"Welcome to the server!")
        print(f"Connected by {addr}")
        data = connect.recv(1024)
        print(data.decode())
        msg = input()
        connect.send(msg.encode())
        
