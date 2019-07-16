from threading import Thread
import time
import socket
from multiprocessing.pool import ThreadPool
import sys
sv=sys.argv[0]
sv=sv[sv.find('_')+1:]
sv=sv[:sv.find('.py')]
pool = ThreadPool(processes=1)
timeout=100
def handle_client(c, addr):
	print ('connection from  : '+addr[0])
	f=open("log.txt",'a')
	f.write("\t[+]  get connection from "+addr[0]+" Server veriosn "+sv)
	f.write("\t\n")
	f.write("\t\t"+time.strftime("%H:%M:%S - %d/%h/%Y"))
	f.write("\t\n")
	f.close()
	st=time.time()
	while True and time.time()-st<timeout:
		l=c.recv(1024)
		if l==b'lZ123Fgf12nnzoe124@zer!' or l=="lZ123Fgf12nnzoe124@zer!":
			print("shut_down_request")
			f=open("log.txt",'a')
			f.write("\t[!] shut down request "+addr[0])
			f.write("\t\n")
			f.write("\t\t"+time.strftime("%H:%M:%S - %d/%h/%Y"))
			f.write("\t\n")
			f.close()
			c.send('YES_Shut_down'.encode('UTF-8'))
			return "Shut"
		print(l)
		c.send('YES'.encode('UTF-8'))
		time.sleep(1)
	for ci in c_list:
		if ci==c:
			ci[0].close()

	f=open("log.txt",'a')
	f.write("\t[-] close connection timeout "+addr[0])
	f.write("\t\n")
	f.write("\t\t"+time.strftime("%H:%M:%S - %d/%h/%Y"))
	f.write("\t\n")
	f.close()
def main(s):
	host = socket.gethostbyname(socket.gethostname())  # Get local machine name
	port = 5132                # Reserve a port for your service.
	s.bind((host, port))        # Bind to the port
	print("Server "+sv+" started : "+host)
	f=open("log.txt",'a')
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
			f=open("log.txt",'a')
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


if __name__=='__main__':
	while True:
		try:
			soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)         # Create a socket object
			c_list=[]
			r=main(soc)
			if r=='Shut':
				print("shut_dows_server")
				f=open("log.txt",'a')
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
			f=open("log.txt",'a')
			f.write("\t[!] connection problem server")
			f.write("\n")
			f.write("\t\t"+str(e))
			f.write("\n")
			f.write("\t\t"+time.strftime("%H:%M:%S - %d/%h/%Y"))
			f.write("\n")
			f.close()
			soc.close()
