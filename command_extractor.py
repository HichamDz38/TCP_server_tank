# -*- coding: utf-8 -*-
import time

class Header():
	def __init__(Id,Property,T_Id,Sn,Body_length,connection):
		self.Id=Id
		self.Property=Property
		self.Body_length=Body_length
		self.connection=connection
		self.T_Id=T_Id
		self.Sn=Sn

class Message_basic():
	def __init__(Alert,Status,Latitude,Longitude,Length,Speed,Direction,Time):
		self.Alert=Alert
		self.Status=Status
		self.Latitude=Latitude
		self.Longitude=Longitude
		self.Length=Length
		self.Speed=Speed
		self.Direction=Direction
		self.Time=Time

def ut8_hex(cmd):
	N_command=[]
	for c in cmd:
		N_command.append(eval(hex(ord(c))))
	return N_command

def get_extra_data(cmd):
	try:
		if cmd[0]==0x01:
			#print(int('{:02x}{:02x}{:02x}{:02x}'.format(cmd[2],cmd[3],cmd[4],cmd[5]),16))
			return {'Milage':int('{:02x}{:02x}{:02x}{:02x}'.format(cmd[2],cmd[3],cmd[4],cmd[5]),16)}
		elif cmd[0]==0x02:
			#print('02',cmd)
			return {'Oil_qualtity':int('{:02x}{:02x}'.format(cmd[2],cmd[3]),16)}
		elif cmd[0]==0x33:
			#print('33',cmd)
			lengt=cmd[1]
			KMD=cmd[10:2+lengt]
			#print(KMD)
			"""for i in KMD:
				print(chr(i),end="")
			print()"""
			Lock_status=int(chr(KMD[0]))
			Seal_status=int(chr(KMD[1]))
			Battery=int(chr(KMD[2])+chr(KMD[3])+chr(KMD[4]))
			Tamper_status=int(chr(KMD[5]))
			Repport_reason=chr(KMD[6])
			Operational_ID=''
			C=7
			while KMD[C]!=38:
				Operational_ID+=chr(KMD[C])
				C+=1
			Sub_lock_state=''
			C+=1
			while KMD[C]!=38:
				Sub_lock_state+=chr(KMD[C])
				C+=1
			User_busness_ID=''
			C+=1
			while KMD[C]!=35:
				User_busness_ID+=chr(KMD[C])
				C+=1
			return {
				"Lock_status":Lock_status,
				"Seal_status":Seal_status,
				"Battery":Battery,
				"Tamper_status":Tamper_status,
				"Repport_reason":Repport_reason,
				"Operational_ID":Operational_ID,
				"Sub_lock_state":Sub_lock_state,
				"User_busness_ID":User_busness_ID}
		elif cmd[0]==0x34:
			return None
			print("get 0x34 message {} ".format(cmd))
		elif cmd[0]==0x35:
			return None
			print("get 0x35 message {} ".format(cmd))
		else:
			print("get unkown message format {}".format(cmd))
			return False
	except Exception as e:
		print("exception get_extra_data {}".format(e))
		print(cmd)
		return None
def get_data(cmd):
	try:
		message_id=cmd[1:3]
		if message_id==[2,0]:
			m_length=cmd[3:5]
			T_Id=cmd[5:11]
			message_sn=cmd[11:13]
			alert=cmd[13:17]
			status=cmd[17:21]
			latitude=cmd[21:25]
			longitude=cmd[25:29]
			length=cmd[29:31]
			speed=cmd[31:33]
			direction=cmd[33:35]
			tim=cmd[35:41]
			"""
			print('next message code ',cmd[41])
			print('next message length ',cmd[42])
			print('next message code ',cmd[42+5])
			print('next message length ',cmd[42+6])
			"""
			#message_id='{:02x}{:02x}'.format(message_id[0],message_id[1])
			Conn_pro = m_length[0]&252
			Conn_type= m_length[0]&2
			Terminal_ID='{:02x}{:02x}{:02x}{:02x}{:02x}{:02x}'.format(T_Id[0],T_Id[1],T_Id[2],T_Id[3],T_Id[4],T_Id[5])
			#message_sn='{:02x}{:02x}'.format(message_sn[0],message_sn[1])
			Alert=int('{:02x}{:02x}{:02x}{:02x}'.format(alert[0],alert[1],alert[2],alert[3]),16)
			Status=int('{:02x}{:02x}{:02x}{:02x}'.format(status[0],status[1],status[2],status[3]),16)
			Latitude=int('{:02x}{:02x}{:02x}{:02x}'.format(latitude[0],latitude[1],latitude[2],latitude[3]),16)/1000000
			Longitude=int('{:02x}{:02x}{:02x}{:02x}'.format(longitude[0],longitude[1],longitude[2],longitude[3]),16)/1000000
			Length=int('{:02x}{:02x}'.format(length[0],length[1]),16)
			Speed=int('{:02x}{:02x}'.format(speed[0],speed[1]),16)
			Direction=int('{:02x}{:02x}'.format(direction[0],direction[1]),16)
			Time='20{:02x}-{:02x}-{:02x} {:02x}:{:02x}:{:02x}'.format(tim[0],tim[1],tim[2],tim[3],tim[4],tim[5])
			"""
			print('message ID {:02x}{:02x}'.format(message_id[0],message_id[1]))
			print('message length {} '.format((m_length[0]&3)*256+m_length[1]))
			print('connection property {}'.format(m_length[0]&252))
			print('connection type {}'.format(m_length[0]&2))
			print('Terminal ID {:02x} {:02x} {:02x} {:02x} {:02x} {:02x}'.format(T_Id[0],T_Id[1],T_Id[2],T_Id[3],T_Id[4],T_Id[5]))
			print('message sn {:02x}{:02x}'.format(message_sn[0],message_sn[1]))
			print('Alert {:02x}{:02x} {:02x}{:02x} {}'.format(alert[0],alert[1],alert[2],alert[3],Alert))
			print('Status {:02x}{:02x} {:02x}{:02x} {}'.format(status[0],status[1],status[2],status[3],Status))
			print('latitude {:02x}{:02x} {:02x}{:02x} {}'.format(latitude[0],latitude[1],latitude[2],latitude[3],Latitude))
			print('longitude {:02x}{:02x} {:02x}{:02x} {}'.format(longitude[0],longitude[1],longitude[2],longitude[3],Longitude))
			print('length {:02x}{:02x} {}'.format(length[0],length[1],Length))
			print('speed {:02x}{:02x} {}'.format(speed[0],speed[1],Direction))
			print('direction {:02x}{:02x} {}'.format(direction[0],direction[1],Speed))
			print('Time     : 20{:02x}-{:02x}-{:02x} {:02x}:{:02x}:{:02x}'.format(tim[0],tim[1],tim[2],tim[3],tim[4],tim[5]))
			"""
			header={
				'message_id':message_id,
				'message_sn':message_sn,
				'Terminal_id':T_Id,
				"link":'http://www.monitor-rwc.ml//post.php'
			}

			data={
				'Terminal_ID':Terminal_ID,
				'alert':Alert,
				'status':Status,
				'latitude':Latitude,
				'longitude':Longitude,
				'length':Length,
				'speed':Speed,
				'direction':Direction,
				'time':Time
			}
			ind=41
			MMM=(m_length[0]&3)*256+m_length[1]
			header['number_message']=1
			while ind<MMM-2:
				#print(cmd[ind],cmd[ind+1])
				LT=get_extra_data(cmd[ind:ind+2+cmd[ind+1]])
				if LT:
					data.update(LT)
				else: 
					print("error data {}\n{}".format(cmd,cmd[ind:ind+2+cmd[ind+1]]))
				ind=ind+2+cmd[ind+1]
				
			return [header,[data]]
		elif message_id==[2,16]:
			#print("get message batch")
			m_length=((cmd[3]&3)*256)+cmd[4]
			#print('message length ',m_length)
			T_Id=cmd[5:11]
			message_sn=cmd[11:13]
			ind=13
			header={
					'message_id':message_id,
					'message_sn':message_sn,
					'Terminal_id':T_Id,
					"link":'http://www.monitor-rwc.ml//post.php'
				}
			#print('header ',header)
			#print(cmd[ind])
			Data=[]
			number_message=0
			while ind<m_length-2:
				leng=cmd[ind]
				#print('sub_batch message length ',leng)
				#time.sleep(2)
				alert=cmd[ind+1:ind+5]
				status=cmd[ind+5:ind+9]
				latitude=cmd[ind+9:ind+13]
				longitude=cmd[ind+13:ind+17]
				length=cmd[ind+17:ind+19]
				speed=cmd[ind+19:ind+21]
				direction=cmd[ind+21:ind+23]
				tim=cmd[ind+23:ind+29]
				#print(tim)
				Terminal_ID='{:02x}{:02x}{:02x}{:02x}{:02x}{:02x}'.format(T_Id[0],T_Id[1],T_Id[2],T_Id[3],T_Id[4],T_Id[5])
				Alert=int('{:02x}{:02x}{:02x}{:02x}'.format(alert[0],alert[1],alert[2],alert[3]),16)
				Status=int('{:02x}{:02x}{:02x}{:02x}'.format(status[0],status[1],status[2],status[3]),16)
				Latitude=int('{:02x}{:02x}{:02x}{:02x}'.format(latitude[0],latitude[1],latitude[2],latitude[3]),16)/1000000
				Longitude=int('{:02x}{:02x}{:02x}{:02x}'.format(longitude[0],longitude[1],longitude[2],longitude[3]),16)/1000000
				Length=int('{:02x}{:02x}'.format(length[0],length[1]),16)
				Speed=int('{:02x}{:02x}'.format(speed[0],speed[1]),16)
				Direction=int('{:02x}{:02x}'.format(direction[0],direction[1]),16)
				Time='20{:02x}-{:02x}-{:02x} {:02x}:{:02x}:{:02x}'.format(tim[0],tim[1],tim[2],tim[3],tim[4],tim[5])
				#print(Time)
				ind=ind+leng+1
				data={
					'Terminal_ID':Terminal_ID,
					'alert':Alert,
					'status':Status,
					'latitude':Latitude,
					'longitude':Longitude,
					'length':Length,
					'speed':Speed,
					'direction':Direction,
					'time':Time
				}
				number_message+=1
				#time.sleep(2)
				Data.append(data)
				#print(Data)
			header['number_message']=number_message
			return [header,Data]
		elif message_id==[3,19]:
			Message_body=cmd[3:5]
			T_Id=cmd[5:11]
			Terminal_ID='{:02x}{:02x}{:02x}{:02x}{:02x}{:02x}'.format(T_Id[0],T_Id[1],T_Id[2],T_Id[3],T_Id[4],T_Id[5])
			message_sn=cmd[11:13]
			N_param=cmd[13:15]
			param_Total=cmd[15]
			ind=16
			data={"Terminal_ID":Terminal_ID}
			commands=[]
			while ind<len(cmd)-2:
				x={
					str(cmd[ind]):get_command(cmd[ind],cmd[ind+2:ind+cmd[ind+1]+2])
				}
				data.update(x)
				ind+=cmd[ind+1]+2
			header={
					'message_id':message_id,
					'message_sn':message_sn,
					'Terminal_id':T_Id,
					"link":'http://www.monitor-rwc.ml//config.php'
				}
			header['number_message']=1
			print("get  query responce")
			print("_"*15)
			print(data)
			print("_"*15)
			return [header,[data]]
		else:
			print("error message typecnot support yet")
			print("message_id :",message_id)
			return [None,None]
	except Exception as e:
		print("exception get data {}".format(e))
		return [None,None]
def get_command(x,y):
	if x==1:
		return '{:02x}{:02x}{:02x}{:02x}{:02x}{:02x}'.format(y[0],y[1],y[2],y[3],y[4],y[5])
	elif x==2:
		return y[0]*256+y[1]
	elif x==3:
		S=""
		for i in y:
			S+=chr(i)
		return S
	elif x==4:
		S=""
		for i in y:
			S+=chr(i)
		return S
	elif x==5:
		S=""
		for i in y:
			S+=chr(i)
		return S
	elif x==6:
		return y[0]*256+y[1]
	elif x==7:
		return y
	elif x==8:
		return y[0]*256+y[1]
	elif x==9:
		S=""
		for i in y:
			S+=chr(i)
		return S
	elif x==0x0A:
		S=""
		for i in y:
			S+=chr(i)
		return S
	elif x==0x0B:
		S=""
		for i in y:
			S+=chr(i)
		return S
	elif x==0x0C:
		S=""
		for i in y:
			S+=chr(i)
		return S
	elif x==0x0D:
		S=""
		for i in y:
			S+=chr(i)
		return S
	elif x==0x0E:
		S=""
		for i in y:
			S+=chr(i)
		return S
	elif x==0x0F:
		return y
	elif x==0x10:
		return y
	elif x==0x11:
		return y[0]*256+y[1]
	elif x==0x12:
		S=""
		for i in y:
			S+=chr(i)
		return S
	elif x==0x13:
		S=""
		for i in y:
			S+=chr(i)
		return S
	elif x==0x14:
		return y[0]*256+y[1]
	elif x==0x15:
		S=""
		for i in y:
			S+=chr(i)
		return S[:4]+'-'+S[4:6]+'-'+S[6:8]+" "+S[8:10]+":"+S[10:12]+":"+S[12:]
	elif x==0x16:
		return y
	elif x==0x17:
		S=""
		for i in y:
			S+=chr(i)
		return S
	elif x==0x18:
		S=""
		for i in y:
			S+=chr(i)
		return S
	elif x==0x19:
		S=""
		for i in y:
			S+=chr(i)
		return S
	elif x==0x1A:
		S=""
		for i in y:
			S+=chr(i)
		return S
	elif x==0x1B:
		S=""
		for i in y:
			S+=chr(i)
		return S
	elif x==0x1C:
		S=""
		for i in y:
			S+=chr(i)
		return S
	elif x==0x1D:
		S=""
		for i in y:
			S+=chr(i)
		return S
	elif x==0x1E:
		S=""
		for i in y:
			S+=chr(i)
		return S
	elif x==0x1F:
		S=""
		for i in y:
			S+=chr(i)
		return S
	elif x==0x20:
		S=""
		for i in y:
			S+=chr(i)
		return S
	elif x==0x21:
		S=""
		for i in y:
			S+=chr(i)
		return S
	elif x==0x22:
		S=""
		for i in y:
			S+=chr(i)
		return S
	elif x==0x23:
		return y
	elif x==0x24:
		return y
	elif x==0x25:
		return y[0]*256+y[1]
	elif x==0x26:
		S=""
		for i in y:
			S+=chr(i)
		return S
	elif x==0x27:
		return y[0]*256+y[1]
	elif x==0x28:
		S=""
		for i in y:
			S+=chr(i)
		return S
	elif x==0x29:
		S=""
		for i in y:
			S+=chr(i)
		return S
	elif x==0x2A:
		S=""
		for i in y:
			S+=chr(i)
		return S
	elif x==0x2B:
		S=""
		for i in y:
			S+=chr(i)
		return S
	elif x==0x33:
		return y
	elif x==0x34:
		S=""
		for i in y:
			S+=chr(i)
		return S
	elif x==0x35:
		S=""
		for i in y:
			S+=chr(i)
		return S
	elif x==0x36:
		S=""
		for i in y:
			S+=chr(i)
		return S
	elif x==0x37:
		return y
	elif x==0x38:
		S=""
		for i in y:
			S+=chr(i)
		return S

def check_command(cmd):
	#print(cmd)
	if cmd[0]!=0x7e:
		print("error start byte {:02} {:02x}".format(cmd[0],cmd[0]))
		return False
	if cmd[-1]!=0x7e:
		print("error end byte {:02} {:02x}".format(cmd[-1],cmd[-1]))
		return False
	if len(cmd)<40:
		print("error message too small")
		return False
	code=0
	for c in cmd[1:-2]:
		code^=c
	if code==cmd[-2]:
		return True
	else:
		print("error verification code {} != {}".format(code,cmd[-2]))
		print(cmd)
		return False

def main():
	import Send_device_data
	while True:
		command=input()
		if command=='exit':
			return
		if ' ' in command:
			command=command.split()
		else:
			L2=[]
			for i in range(0,len(command),2):
				L2.append(command[i:i+2])
			command=L2
		L2=list(map(lambda x:int(x,16),command))
		if(check_command(L2)):
			print('correct packet')
			gt=get_data(L2)
			print(gt[0])
			print(gt[1])

if __name__=="__main__":
	main()