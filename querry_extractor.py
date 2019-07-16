#cmd=[126, 3, 19, 1, 43, 4, 64, 64, 137, 118, 65, 49, 194, 0, 19, 48, 36, 1, 0, 1, 6, 4, 64, 64, 137, 118, 65, 2, 2, 0, 0, 3, 11, 52, 53, 46, 51, 53, 46, 49, 50, 46, 57, 50, 4, 0, 5, 4, 53, 49, 51, 50, 6, 2, 0, 30, 7, 1, 3, 8, 2, 0, 195, 9, 20, 105, 110, 116, 101, 114, 110, 101, 116, 46, 103, 108, 111, 98, 101, 46, 99, 111, 109, 46, 112, 10, 4, 103, 117, 115, 101, 11, 4, 103, 117, 115, 101, 12, 21, 105, 110, 116, 101, 114, 110, 101, 116, 46, 103, 108, 111, 98, 101, 46, 99, 111, 109, 46, 112, 104, 13, 4, 103, 117, 115, 101, 14, 4, 103, 117, 115, 101, 15, 1, 2, 16, 1, 0, 17, 2, 1, 114, 18, 12, 54, 54, 53, 53, 49, 50, 54, 54, 56, 56, 51, 52, 19, 8, 54, 54, 53, 53, 54, 54, 56, 56, 20, 2, 0, 180, 21, 14, 50, 48, 49, 57, 48, 54, 50, 49, 49, 54, 48, 55, 50, 56, 22, 1, 2, 23, 0, 24, 0, 25, 0, 26, 0, 27, 0, 28, 0, 29, 0, 30, 0, 31, 0, 32, 0, 33, 0, 34, 0, 35, 1, 0, 38, 8, 49, 50, 51, 52, 49, 50, 51, 52, 39, 2, 0, 0, 40, 9, 49, 54, 0, 0, 0, 0, 0, 0, 0, 41, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 42, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 43, 9, 52, 52, 53, 53, 54, 54, 55, 55, 255, 51, 0, 53, 9, 71, 52, 50, 48, 45, 55, 54, 52, 49, 54, 8, 48, 48, 48, 48, 48, 48, 48, 48, 55, 1, 27, 58, 6, 0, 0, 0, 5, 0, 10, 59, 2, 0, 0, 39, 126]
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
message_id=cmd[1:3]
Message_body=cmd[3:5]
T_id=cmd[5:11]
message_sn=cmd[11:13]
N_param=cmd[13:15]
param_Total=cmd[15]
ind=16
data={"Terminal_ID":T_id}
commands=[]
while ind<len(cmd)-2:
	x={
		str(cmd[ind]):get_command(cmd[ind],cmd[ind+2:ind+cmd[ind+1]+2])
	}
	data.update(x)
	ind+=cmd[ind+1]+2
print(data)
print()