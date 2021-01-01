import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('127.0.0.1', 55555))
# how many bite your want to receive from server
message = s.recv(1024)

s.close()

print(message.decode())
