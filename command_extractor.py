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
				'Terminal_id':T_Id
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
			header['number_message']=0
			while ind<MMM-2:
				#print(cmd[ind],cmd[ind+1])
				LT=get_extra_data(cmd[ind:ind+2+cmd[ind+1]])
				if LT:
					data.update(LT)
					header['number_message']+=1
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
					'Terminal_id':T_Id
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
			print("get  query responce")
			print("add support in the next version")
			print(cmd)
		else:
			print("error message typecnot support yet")
			print("message_id :",message_id)
			return [None,None]
	except Exception as e:
		print("exception get data {}".format(e))
		return [None,None]

def check_command(cmd):
	#print(cmd)
	if cmd[0]!=0x24:
		print("error start byte {:02} {:02} {:02x} {:02x}".format(cmd[0],cmd[1],cmd[0],cmd[1]))
		return False
	if cmd[1]!=0x24:
		print("error start byte {:02} {:02} {:02x} {:02x}".format(cmd[0],cmd[1],cmd[0],cmd[1]))
		return False
	if cmd[-1]!=0x0d:
		print("error end byte {:02} {:02x}".format(cmd[-1],cmd[-1]))
		return False
	if len(cmd)<40:
		print("error message too small")
		return False
	code=0
	for c in cmd[2:-2]:
		code^=c
	if code==cmd[-2]:
		return True
	else:
		print("error verification code {} != {}".format(code,cmd[-2]))
		print(cmd)
		return False

def Position_parser(cmd):
	length=cmd[3:5]
	T_Id=cmd[5:9]
	tim=cmd[9:15]
	latitude=cmd[15:19]
	longitude=cmd[19:23]
	speed=cmd[23:25]
	direction=cmd[25:27]
	gps=cmd[27:28]
	detection=cmd[28:29]
	ignition=cmd[29:30]
	oil=cmd[30:32]
	voltage=cmd[44:46]#cmd[32:34]
	mileage=cmd[34:38]
	temperature=cmd[38:40]

	print('message length {} '.format(length[0]*256+length[1]))
	print('Terminal ID {:02x} {:02x} {:02x} {:02x}'.format(T_Id[0],T_Id[1],T_Id[2],T_Id[3]))
	print('latitude {}{}{}'.format(latitude[1],latitude[2],latitude[3]))
	print('longitude {}{}{}'.format(longitude[1],longitude[2],longitude[3]))
	print('length {:02x}{:02x} {}'.format(length[0],length[1],length))
	print('speed {:02x}{:02x} {}'.format(speed[0],speed[1],speed))
	print('direction {:02x}{:02x} {}'.format(direction[0],direction[1],direction))
	print('Time     : 20{:02x}-{:02x}-{:02x} {:02x}:{:02x}:{:02x}'.format(tim[0],tim[1],tim[2],tim[3],tim[4],tim[5]))
	print('id')
	Terminal_ID='{:02x}{:02x}{:02x}{:02x}'.format(T_Id[0],T_Id[1],T_Id[2],T_Id[3])
	print('time')
	Time='20{:02x}-{:02x}-{:02x} {:02x}:{:02x}:{:02x}'.format(tim[0],tim[1],tim[2],tim[3],tim[4],tim[5])
	print('latitude')
	Latitude=int('{:02x}{:02x}{:02x}'.format(latitude[1]%16,latitude[2],latitude[3]))/60000+int('{:02x}{:02x}'.format(latitude[0],latitude[1]//16))
	print('longitude')
	Longitude=int('{:02x}{:02x}{:02x}'.format(longitude[1]%16,longitude[2],longitude[3]))/60000+int('{:02x}{:02x}'.format(longitude[0],longitude[1]//16))
	print('Speed')
	Speed=speed[0]*100+speed[1]
	print('Direction')
	Direction=direction[0]*100+direction[1]
	print('gps')
	Gps=gps
	print('detectio')
	Detection=detection
	print('ignition')
	Ignition=ignition
	print('oil_resistor')
	Oil=int('{:02x}{:02x}'.format(oil[0],oil[1]),16)/10
	print('voltage')
	Voltage=int(voltage[0])*16+int(voltage[1])
	print(Terminal_ID,Latitude,Longitude,Voltage,Time)
	return [Terminal_ID,Latitude,Longitude,Voltage,Time,Speed,Direction,Gps,Detection,Ignition,Oil]
	
def get_command(cmd):
	if cmd[2]==0x21:
		print("Heart beat packet function")
	elif cmd[2]==0x80:
		print("Position data")
		return Position_parser(cmd)
	elif cmd[2]==0x81:
		print("The return of rollcall")
	elif cmd[2]==0x82:
		print("Alarm data")
	elif cmd[2]==0x83:
		print("The data of terminal's status")
	elif cmd[2]==0x84:
		print("Message to center")
	elif cmd[2]==0x85:
		print("Terminal's answer data")
	elif cmd[2]==0x8E:
		print("The blind area data of GPRS")
		return Position_parser(cmd)
	elif cmd[2]==0x54:
		print("The Trasmission of the picture frame")
	elif cmd[2]==0x56:
		print("the response of camera")
	elif cmd[2]==0x57:
		print("Picture data")
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
