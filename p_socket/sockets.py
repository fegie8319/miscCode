import socket

# AF_INET = 宣告為online socket ; SOCK_STREAM = 宣告網路協議
# this is a socket work with TCP in this internet socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# the ip and port we want the socket to run
s.bind(('127.0.0.1', 55555))

s.listen()

while True:
    client, address = s.accept()
    print("Connected to {}".format(address))
    client.send("You are connected!".encode())
    client.close()
