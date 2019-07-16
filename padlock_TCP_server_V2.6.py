#!/bin/python3.6
from threading import Thread
import time
import socket
from multiprocessing.pool import ThreadPool
import sys
from command_extractor import *
from Send_device_data import *
import struct
import select
global plat_M_SN
sv=sys.argv[0]
sv=sv[sv.find('_')+1:]
sv=sv[:sv.find('.py')]
pool = ThreadPool(processes=1)
timeout=30
global  ecode
ecode=-1
def handle_client(c, addr):
	global  ecode
	ecode=0
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
	ecode=1
	while True and time.time()-st<timeout:
		l=[]
		Ll=[]
		n=0
		st2=time.time()
		while n<2 and time.time()-st2<20:
			lll=c.recv(1)
			ecode=lll
			if not(lll):
				return
			val=int.from_bytes(lll,byteorder="big")
			#Ll+=lll
			ll=val#ord(lll)
			#print('{:02x}'.format(ll),end=' ')
			if ll==0x7e:
				n+=1
			l.append(ll)
			Ll.append(hex(ll)[2:])
		#print()
		#print(' '.join(Ll))
		ecode=l
		if n<2:continue
		#print(l)
		log=time.strftime("command_%d_%h_%Y.txt")
		f=open(log,'a')
		f.write("\t[!] get command from "+addr[0])
		f.write("\t\n")
		f.write("\t\t"+time.strftime("%H:%M:%S - %d/%h/%Y"))
		f.write("\t\n")
		for i in l or []:
			f.write('{:02x} '.format(i))
		f.write("\t\n")
		f.close()
		#l=ut8_hex(l)
		l2=list(map(lambda x:hex(x)[2:].rjust(2,'0'),l))
		#print(l)
		if (check_command(l)):
			h,d=get_data(l)
			ecode=(h,d)
			if not(h) or not(d):
				return false
			ecode=d[0]
			if d[0]['Terminal_ID'] not in sr_list:
				sr_list.append(d[0]['Terminal_ID'])
			ecode=sr_list
			R=0
			for hi in range(h['number_message']):
				#print("send data")
				#print()
				#print(d[hi]['Terminal_ID'])
				#print("{} {}".format('http://www.monitor-rwc.ml//post.php',d[hi]))
				ecode=d[hi]
				try:
					r=send_data(d[hi],h["link"])
					ecode=r
					if r:
						print("response : {} {}".format(r,r[-1]))
						R=R|int(r[-1])
					else:
						print("error response ")
				except Exception as e:
					print("connexion problem with the website : {} {} {}".format(h["link"],d[hi]),e)
			ecode=(h,d)
			print("Terminal ID {}".format(d[0]['Terminal_ID']))
			#print(sr_list)
			#print(R)
			m=[0x80,0x01,0x00,0x05,]+h['Terminal_id']+[plat_M_SN//256,plat_M_SN%256]+h['message_sn']+h['message_id']
			#print(m)
			code=0
			for i in m:
				code^=i
			M=[0x7e]+m+[int(r[-1])]+[code]+[0x7e]
			M2=list(map(lambda x:hex(x)[2:].rjust(2,'0'),M))
			#print(' '.join(M2))
			#print('-----------------------------------------------------------------------------')
			for ik in M:
				#MM+=chr(ik)
				val = bytes([ik])
				c.send(val)
			#c.sendall(MM.encode('UTF-8'))
			#print(M)
			plat_M_SN=(plat_M_SN+1)%65536
			#print(h['Terminal_id'],querry_list.keys())
			if d[0]['Terminal_ID'] not in querry_list.keys():
				print('test Terminal Query')
				#m=[0x03,0x10,0x00,0x04,]+h['Terminal_id']+[plat_M_SN//256,plat_M_SN%256]+[0x01,0x24,0x01,0x00]

				m=[3, 18, 0, 49]+h['Terminal_id']+[plat_M_SN//256,plat_M_SN%256]+[48, 36, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 38, 39, 40, 41, 42, 43, 51, 53, 54, 55, 58, 59]
				code=0
				for i in m:
					code^=i
				M=[0x7e]+m+[code]+[0x7e]
				print(M)
				time.sleep(10)
				M2=list(map(lambda x:hex(x)[2:].rjust(2,'0'),M))
				#print(M2)
				for ik in M:
					#MM+=chr(ik)
					val = bytes([ik])
					c.send(val)
				plat_M_SN=(plat_M_SN+1)%65536
				querry_list[d[0]['Terminal_ID']]=0
			else:
				querry_list[d[0]['Terminal_ID']]+=1
				if querry_list[d[0]['Terminal_ID']]>50:
					del querry_list[d[0]['Terminal_ID']]
			
			"""
			print("get_command back from :",addr[0])
			l=[]
			Ll=[]
			n=0
			st2=time.time()
			while n<2 and time.time()-st2<20:
				lll=c.recv(1)
				if len(lll)==0:
					return
				val=int.from_bytes(lll,byteorder="big")
				#Ll+=lll
				ll=val#ord(lll)
				#print('{:02x}'.format(ll),end=' ')
				if ll==0x7e:
					n+=1
				l.append(ll)
				Ll.append(hex(ll)[2:])
			print()
			print(' '.join(Ll))
			"""

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
				val = bytes([ord(mi)])
				c.send(val)
			#c.send('YES_Shut_down'.encode('UTF-8'))
			return "Shut"
		else:
			m='~ERROR~'
			for mi in m:
				val = bytes([ord(mi)])
				c.send(val)
		time.sleep(1)
	for ci in c_list or []:
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
	global  ecode
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
		is_readable = [s]
		is_writable = []
		is_error = []
		r, w, e = select.select(is_readable, is_writable, is_error, 1.0)
		if r:
			c, addr = s.accept()
			c_list.append(addr[0])
			print("client connected")
			#print(c_list)
			print("_________________________________________________________________")
			try:
				mn=pool.apply_async(handle_client,(c, addr))
				#mn=Thread(target=handle_client,args=(c, addr,)).start()
				if not(mn):
					c.close()
				elif mn.get()=='Shut':
					return "Shut"
				else:
					c.close()
			except Exception as e:
				print("{} client Error {}".format(e,ecode))
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
				for ci in c_list or []:
					if ci==c:
						ci[0].close()
				"""
				from command_extractor import *
				from Send_device_data import *
				"""
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
			sr_list=[]
			querry_list={}
			r=main(soc)
			if r=='Shut':
				print("shut_dows_server")
				log=time.strftime("log_%d_%h_%Y.txt")
				f=open(log,'a')
				f.write("\t[-] shut down server")
				f.write("\t\n")
				f.write("\t\t"+time.strftime("%H:%M:%S - %d/%h/%Y"))
				f.write("\t\n")
				for ci in c_list or []:
					print(ci)
					print("close connection "+ci[1][0])
					f.write("\t\t[-] close connection "+ci[1][0])
					f.write("\t\n")
					ci[0].close()
				f.close()
				soc.close()
				break
		except Exception as e:
			print("{} socket error".format(e))
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
