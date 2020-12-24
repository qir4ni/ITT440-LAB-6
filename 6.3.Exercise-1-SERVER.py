import socket
import sys
import time
import errno
import math
from multiprocessing import Process


print(r"""
-----------------------------------------
 __________
| ________ |    Oleh Awis Qirani (qir4ni)
||12345678||	Disember 2020
|----------|     _____      _            _       _
|[M|#|C][-]|    / ____|    | |          | |     | |
|[7|8|9][+]|   | |     __ _| | ___ _   _| | __ _| |_ ___  _ __
|[4|5|6][x]|   | |    / _` | |/ __| | | | |/ _` | __/ _ \| '__|
|[1|2|3][%]|   | |___| (_| | | (__| |_| | | (_| | || (_) | |
|[.|O|:][=]|    \_____\__,_|_|\___|\__,_|_|\__,_|\__\___/|_|
|----------|
	     Server Version
-----------------------------------------
               """)

def calcLog(x, base):
	print(f"[+] Calculating logarithm for {x} with base {base}")
	x = int(x)
	base = int(base)
	try:
		if(str(base) == None or str(base) == " "):
			answer = math.log(x)
		else:
			answer = math.log(x, base)
	except:
		answer = "unable to be calculated. Please retry again.."

	return answer

def calcSqrt(x):
	print(f"[+] Calculating square root of {x}")
	x = int(x)
	if(x >= 0):
		try:
			answer = math.sqrt(x)
		except:
			answer = "unable to be calculated. Please retry again.."
	else:
		answer = "unable to be calculated because it is a negative value."

	return answer

def calcExp(x):
	print(f"[+] Calculating exponential of {x}")
	x = float(x)
	try:
		answer = math.exp(x)
	except:
		answer = "unable to be calculated. Please retry again.."

	return answer


def process_start(s_sock):
	s_sock.send(str.encode('[+] Welcome to the Server\n'))
	while True:
		data = s_sock.recv(2048)
		#print(data)
		data = data.decode('utf-8')
		try:
			option, value1, value2 = data.split(" ", 3)
		except:
			print("[+] Unable to calculate, client disconnected\n")
		#print(option, value1, value2)
		#data = data.decode('utf-8')
		#print(data)
		if not data:
			break
		#if(data == 'a'):
		#	print("Hello World")

		if(option == 'log'):
			answer = calcLog(value1, value2)
		elif(option == 'sqrt'):
			answer = calcSqrt(value1)
		elif(option == 'exp'):
			answer = calcExp(value1)

		message = "[+] The answer is  %s." % str(answer)
		print("[+] Completed\n------------------------------------\n")
		s_sock.sendall(str.encode(message))

		#s_sock.sendall(str.encode(ok_message))
	s_sock.close()

if __name__ == '__main__':
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.bind(("", 8888))
	print("[+] Listening for input from clients...")
	s.listen(3)
	try:
		while True:
			try:
				s_sock, s_addr = s.accept()
				p = Process(target = process_start, args = (s_sock,))
				p.start()

			except socket.error:
				print('[+] Got a socket error')

	except Exception as e:
		print('[+] An exception occured!')
		print(e) 
		sys.exit(1)

	finally:
		s.close()
