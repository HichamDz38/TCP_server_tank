from threading import Thread
import time
import socket
from multiprocessing.pool import ThreadPool
import sys
from command_extractor import *
from Send_device_data import *
import struct
global plat_M_SN
sv=sys.argv[0]
sv=sv[sv.find('_')+1:]
sv=sv[:sv.find('.py')]
pool = ThreadPool(processes=1)
timeout=30
def handle_client(c, addr):
	global plat_M_SN
	print ('connection from  : '+addr[0])
	log=time.strftime("log_%d_%h_%Y.txt")
	f=open(log,'a')
	f.write("\t[+]  get connection from "+addr[0]+" Server version "+sv)
	f.write("\t\n")
	f.write("\t\t"+time.strftime("%H:%M:%S - %d/%h/%Y"))
	f.write("\t\n")
	f.close()
	st=time.time()
	while True and time.time()-st<timeout:
		l=[]
		Ll=[]
		n=0
		st2=time.time()
		while n<2 and time.time()-st2<20:
			lll=c.recv(4)
			if len(lll)==0:
				return
			val=struct.unpack('!i', lll[:4])[0]
			#Ll+=lll
			ll=val#ord(lll)
			#print('{:02x}'.format(ll),end=' ')
			if ll==0x7e:
				n+=1
			l.append(ll)
			Ll.append(hex(ll)[2:])
		print()
		print(' '.join(Ll))
		if n<2:continue
		#print(l)
		log=time.strftime("command_%d_%h_%Y.txt")
		f=open(log,'a')
		f.write("\t[!] get command from "+addr[0])
		f.write("\t\n")
		f.write("\t\t"+time.strftime("%H:%M:%S - %d/%h/%Y"))
		f.write("\t\n")
		for i in l:
			f.write('{:02x} '.format(i))
		f.write("\t\n")
		f.close()
		#l=ut8_hex(l)
		l2=list(map(lambda x:hex(x)[2:].rjust(2,'0'),l))
		#print(''.join(l2))
		if (check_command(l)):
			h,d=get_data(l)
			if not(h):
				return
			R=0
			for hi in range(h['number_message']):
				print("send data")
				print()
				print(d[hi])
				r=send_data(d[hi],' http://www.monitor-rwc.ml/post.php')
				print("response : {}".format(r))
				R=R|r
			#print(R)
			m=[0x80,0x01,0x00,0x05,]+h['Terminal_id']+[plat_M_SN//256,plat_M_SN%256]+h['message_sn']+h['message_id']
			code=0
			for i in m:
				code^=i
			M=[0x7e]+m+[r]+[code]+[0x7e]
			print(M)
			print('--------------------------------')
			for ik in M:
				#MM+=chr(ik)
				val = struct.pack('!i', ik)
				c.send(val)
			#c.sendall(MM.encode('UTF-8'))
			plat_M_SN=(plat_M_SN+1)%65536
			#print("end message send")
		elif Ll==['7e', '6c', '5a', '31', '32', '33', '46', '67', '66', '31', '32', '6e', '6e', '7a', '6f', '65', '31', '32', '34', '40', '7a', '65', '72', '21', '7e']:
			print("shut_down_request")
			log=time.strftime("log_%d_%h_%Y.txt")
			f=open(log,'a')
			f.write("\t[!] shut down request "+addr[0])
			f.write("\t\n")
			f.write("\t\t"+time.strftime("%H:%M:%S - %d/%h/%Y"))
			f.write("\t\n")
			f.close()
			m='YES_Shut_down'
			for mi in m:
				val = struct.pack('!i',ord(mi))
				c.send(val)
			#c.send('YES_Shut_down'.encode('UTF-8'))
			return "Shut"
		else:
			m='~ERROR~'
			for mi in m:
				val = struct.pack('!i',ord(mi))
				c.send(val)
		time.sleep(1)
	for ci in c_list:
		if ci==c:
			ci[0].close()

	log=time.strftime("log_%d_%h_%Y.txt")
	f=open(log,'a')
	f.write("\t[-] close connection timeout "+addr[0])
	f.write("\t\n")
	f.write("\t\t"+time.strftime("%H:%M:%S - %d/%h/%Y"))
	f.write("\t\n")
	f.close()
def main(s):
	host = socket.gethostbyname(socket.gethostname())  # Get local machine name
	port = 5132                # Reserve a port for your service.
	s.bind((host, port))        # Bind to the port
	global plat_M_SN
	plat_M_SN=0
	print("Server "+sv+" started : "+host)
	log=time.strftime("log_%d_%h_%Y.txt")
	f=open(log,'a')
	f.write("[+] Server "+sv+" started : "+host)
	f.write("\t\n")
	f.write("\t"+time.strftime("%H:%M:%S - %d/%h/%Y"))
	f.write("\n")
	f.close()
	s.listen(5)                 # Now wait for client connection.
	while True:
		c, addr = s.accept()
		c_list.append((c,addr))
		try:
			mn=pool.apply_async(handle_client,(c, addr))
			#mn=Thread(target=handle_client,args=(c, addr,)).start()
			if mn.get()=='Shut':
				return "Shut"
		except Exception as e:
			print(e)
			log=time.strftime("log_%d_%h_%Y.txt")
			f=open(log,'a')
			f.write("\t[!] connection problem client "+addr[0])
			f.write("\t\n")
			f.write("\t\t"+str(e))
			f.write("\t\n")
			f.write("\t\t"+time.strftime("%H:%M:%S - %d/%h/%Y"))
			f.write("\n")
			f.close()
			for ci in c_list:
				if ci==c:
					ci[0].close()
	s.close()                # Close the connection
def timing():
	time.sleep(60)
	#soc.close()
	sys.exit()

if __name__=='__main__':
	#Thread(target=timing).start()
	while True:
		try:
			soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)         # Create a socket object
			#soc.settimeout(1)
			c_list=[]
			r=main(soc)
			if r=='Shut':
				print("shut_dows_server")
				log=time.strftime("log_%d_%h_%Y.txt")
				f=open(log,'a')
				f.write("\t[-] shut down server")
				f.write("\t\n")
				f.write("\t\t"+time.strftime("%H:%M:%S - %d/%h/%Y"))
				f.write("\t\n")
				for ci in c_list:
					print("close connection "+ci[1][0])
					f.write("\t\t[-] close connection "+ci[1][0])
					f.write("\t\n")
					ci[0].close()
				f.close()
				soc.close()
				break
		except Exception as e:
			print(e)
			log=time.strftime("log_%d_%h_%Y.txt")
			f=open(log,'a')
			f.write("\t[!] connection problem server")
			f.write("\n")
			f.write("\t\t"+str(e))
			f.write("\n")
			f.write("\t\t"+time.strftime("%H:%M:%S - %d/%h/%Y"))
			f.write("\n")
			f.close()
			soc.close()
			time.sleep(20)
