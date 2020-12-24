import socket
import sys
import time
import errno
import math
from multiprocessing import Process


ok_message = 'HTTP/1.0 200 OK\n\n'
nok_message = 'HTTP/1.0 404 NotFound\n\n'


def calcLog(x, base):

	x = int(x)
	base = int(base)
	try:
		if(str(base) == None or str(base) == " "):
			answer = math.log(x)
		else:
			answer = math.log(x, base)
	except:
		answer = "Error, cannot calculate log. Please retry again.."

	return answer


def process_start(s_sock):
	s_sock.send(str.encode('Welcome to the Server\n'))
	while True:
		data = s_sock.recv(2048)
		print(data)
		data = data.decode('utf-8')
		option, value1, value2 = data.split(" ", 3)
		print(option, value1, value2)
		#data = data.decode('utf-8')
		#print(data)
		if not data:
			break
		#if(data == 'a'):
		#	print("Hello World")

		if(option == 'log'):
			answer = calcLog(value1, value2)

		message = "The answer is  %s." % str(answer)
		s_sock.sendall(str.encode(message))

		#s_sock.sendall(str.encode(ok_message))
	s_sock.close()

if __name__ == '__main__':
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.bind(("", 8888))
	print("listening...")
	s.listen(3)
	try:
		while True:
			try:
				s_sock, s_addr = s.accept()
				p = Process(target = process_start, args = (s_sock,))
				p.start()

			except socket.error:
				print('got a socket error')

	except Exception as e:
		print('an exception occured!')
		print(e) 
		sys.exit(1)

	finally:
		s.close()
