import time
import socket               # Import socket module
from threading import Thread
import sys
import struct
s = socket.socket()         # Create a socket object
#s.settimeout(60)
#address = socket.gethostbyname(socket.gethostname())
#target = socket.gethostname()
#targ="45.35.12.92"#input('enter the server : ')
targ="192.168.32.1"
port = 5133#int(input('enter the port :'))#5132                # Reserve a port for your service.
s.connect((targ, port))        # Bind to the port

print("connected to : {}:{}".format(targ,port))

def main():
	#m=list(map(lambda x:int(x,16),"7E 02 00 00 5D 00 00 00 00 05 31 00 0A 00 00 00 00 00 00 00 03 01 58 F5 22 06 C9 16 B0 00 00 00 00 00 00 19 06 14 11 02 21 01 04 00 00 00 00 33 39 2A 4D 30 30 2C 34 38 2C 31 31 34 31 35 30 47 5A 44 53 45 54 4D 30 30 2D 30 30 26 30 30 30 30 30 30 30 30 30 30 30 30 26 31 32 33 34 35 36 37 38 39 30 31 32 33 34 35 36 23 92 7E".split()))
	m=list(map(lambda x:int(x,16),"24 24 82 00 33 00 34 25 e2 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 47 00 00 00 00 1d 00 00 00 00 00 00 00 00 00 03 00 00 00 00 00 00 00 00 00 08 13 0d ".split()))
	for i in m:
		val = bytes([i])#struct.pack('!b', i)
		s.send(val)
	l=[]
	Ll=b""
	n=0
	st2=time.time()
	while n<2 and time.time()-st2<20:
		lll=s.recv(1)
		val=int.from_bytes(lll,byteorder="big")
		#print(lll,end=" ")
		if len(lll)==0:
			continue
		Ll+=lll
		ll=val#ord(lll)
		#print('{:02x}'.format(ll),end=' ')
		#print(lll,ll)
		if ll==0x7e:
			n+=1
		elif len(l)==0:
			return
		l.append(hex(ll)[2:].rjust(2,'0'))
	print(' '.join(l))
	s.close()
	sys.exit()
	return
def main2():
	while True:
		m=input('enter message to send : ')
		s.send(m.encode('UTF-8'))
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
def timing():
	time.sleep(20)
	s.close()
	sys.exit()
Mm='1'#input('enter le mode 1:list or 2:string ')
if Mm=='1':
	#Thread(target=timing).start()
	main()
elif Mm=='2':
	Thread(target=timing).start()
	main2()

