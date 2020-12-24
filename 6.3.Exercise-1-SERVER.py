import socket
import sys
import time
import errno
from multiprocessing import Process


ok_message = 'HTTP/1.0 200 OK\n\n'
nok_message = 'HTTP/1.0 404 NotFound\n\n'


def process_start(s_sock):
	s_sock.send(str.encode('Welcome to the Server\n'))
	while True:
		option, value1, value2 = s_sock.recv(2048)
		print(option, value1, value2)
		#data = data.decode('utf-8')
		#print(data)
		if not option:
			break
		#if(data == 'a'):
		#	print("Hello World")
		s_sock.sendall(str.encode(ok_message))
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
