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

	status = 0
	while(status == 0):
		option = input('Enter type of operation (log | sqrt | exp): ')
		if(option == 'log'):
			value1 = input("Enter first value: ")
			value2 - input("Enter second value for base: ")
			status = 1
		elif(option == 'sqrt'):
			value1 = input("Enter the value: ")
			value2 = '0'
			status = 1
		elif(option == 'exp'):
			value1 = input("Enter the value: ")
			value2 == '0'
			status = 1
		else:
			print("Invalid operation, please re-enter..")
			status = 0


	Input = option + value1 + value2
	ClientSocket.send(str.encode(Input))
	Response = ClientSocket.recv(1024)
	print(Response.decode('utf-8'))

ClientSocket.close()

