import time
import socket               # Import socket module
from threading import Thread
import sys
import struct
s = socket.socket()         # Create a socket object
s.settimeout(60)
#address = socket.gethostbyname(socket.gethostname())
#target = socket.gethostname()
#targ="45.35.12.92"#input('enter the server : ')
targ="192.168.32.1"#input('enter the server : ')
port = 5132#int(input('enter the port :'))#5132                # Reserve a port for your service.
s.connect((targ, port))        # Bind to the port

print("connected to : {}:{}".format(targ,port))

def main():
	while True:
		m=list(map(lambda x:int(x,16),input('enter message to send : ').split()))
		print(m)
		for i in m:
			s.send(chr(i).encode('UTF-8'))
		l=[]
		Ll=b""
		n=0
		st2=time.time()
		while n<2 and time.time()-st2<20:
			lll=s.recv(1)
			Ll+=lll
			ll=ord(lll)
			print(lll,ll)
			if ll==0x7e:
				n+=1
			l.append(ll)
		print(Ll)
		print(l)
	s.close()

def main2():
	m="~lZ123Fgf12nnzoe124@zer!~"
	for mi in m:
		val = bytes([ord(mi)])
		s.send(val)
	l=[]
	Ll=b""
	n=0
	time.sleep(2)
	s.close()
def timing():
	time.sleep(5)
	s.close()
	sys.exit()
Mm="2"#input('enter le mode 1:list or 2:string ')
if Mm=='1':
	#Thread(target=timing).start()
	main()
elif Mm=='2':
	#Thread(target=timing).start()
	main2()

