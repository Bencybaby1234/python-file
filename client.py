import socket
# getting host name
host = socket.gethostname()
port = 1234

# connesting with server
client = socket.socket()
client.connect((host, port))

# sending message
message = 'hii'
client.send(message.encode())
data = client.recv(1024).decode()
print("recieved from server: "+data)
