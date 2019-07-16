import time
import socket               # Import socket module
from threading import Thread
import sys
import struct
s = socket.socket()         # Create a socket object
#s.settimeout(60)
#address = socket.gethostbyname(socket.gethostname())
#target = socket.gethostname()
targ="45.35.12.92"#input('enter the server : ')
#targ="192.168.32.1"
port = 5132#int(input('enter the port :'))#5132                # Reserve a port for your service.
s.connect((targ, port))        # Bind to the port

print("connected to : {}:{}".format(targ,port))

def main():
	#m=list(map(lambda x:int(x,16),"7E 02 00 00 5D 00 00 00 00 05 31 00 0A 00 00 00 00 00 00 00 03 01 58 F5 22 06 C9 16 B0 00 00 00 00 00 00 19 06 14 11 02 21 01 04 00 00 00 00 33 39 2A 4D 30 30 2C 34 38 2C 31 31 34 31 35 30 47 5A 44 53 45 54 4D 30 30 2D 30 30 26 30 30 30 30 30 30 30 30 30 30 30 30 26 31 32 33 34 35 36 37 38 39 30 31 32 33 34 35 36 23 92 7E".split()))
	m=list(map(lambda x:int(x,16),"7e 03 13 01 2b 04 40 40 89 76 41 65 3e 00 15 30 24 01 00 01 06 04 40 40 89 76 41 02 02 00 00 03 0b 34 35 2e 33 35 2e 31 32 2e 39 32 04 00 05 04 35 31 33 32 06 02 00 1e 07 01 03 08 02 00 c3 09 14 69 6e 74 65 72 6e 65 74 2e 67 6c 6f 62 65 2e 63 6f 6d 2e 70 0a 04 67 75 73 65 0b 04 67 75 73 65 0c 15 69 6e 74 65 72 6e 65 74 2e 67 6c 6f 62 65 2e 63 6f 6d 2e 70 68 0d 04 67 75 73 65 0e 04 67 75 73 65 0f 01 02 10 01 00 11 02 01 72 12 0c 36 36 35 35 31 32 36 36 38 38 33 34 13 08 36 36 35 35 36 36 38 38 14 02 00 b4 15 0e 32 30 31 39 30 36 32 35 30 36 30 33 35 30 16 01 02 17 00 18 00 19 00 1a 00 1b 00 1c 00 1d 00 1e 00 1f 00 20 00 21 00 22 00 23 01 00 26 08 31 32 33 34 31 32 33 34 27 02 00 00 28 09 31 36 00 00 00 00 00 00 00 29 09 00 00 00 00 00 00 00 00 00 2a 09 00 00 00 00 00 00 00 00 00 2b 09 34 34 35 35 36 36 37 37 ff 33 00 35 09 47 34 32 30 2d 37 36 34 31 36 08 30 30 30 30 30 30 30 30 37 01 1b 3a 06 00 00 00 05 00 0a 3b 02 00 00 87 7e".split()))
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

