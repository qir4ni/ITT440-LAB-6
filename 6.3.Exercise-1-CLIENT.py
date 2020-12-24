import socket


ClientSocket = socket.socket()
host = '192.168.1.9'
port = 8888

print('Waiting for connection')
try:
	ClientSocket.connect((host, port))
except socket.error as e:
	print(str(e))

Response =ClientSocket.recv(1024)
print(Response)

while True:
	Input = input('Enter type of operation with first and second value (Example: minus 1 1: ')
	ClientSocket.send(str.encode(Input))
	Response = ClientSocket.recv(1024)
	print(Response.decode('utf-8'))

ClientSocket.close()

