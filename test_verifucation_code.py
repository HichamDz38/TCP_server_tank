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
	print(cmd[1:-2])
	for c in cmd[1:-2]:
		code^=c
	if code==cmd[-2]:
		return True
	else:
		print("error verification code {} != {}".format(code,cmd[-2]))
		print(cmd)
		return False

l=[126, 2, 0, 0, 93, 0, 0, 0, 0, 5, 49, 0, 10, 0, 0, 0, 0, 0, 0, 0, 3, 1, 88, 245, 34, 6, 201, 22, 176, 0, 0, 0, 0, 0, 0, 25, 6, 20, 17, 2, 33, 1, 4, 0, 0, 0, 0, 51, 57, 42, 77, 48, 48, 44, 52, 56, 44, 49, 49, 52, 49, 53, 48, 71, 90, 68, 83, 69, 84, 77, 48, 48, 45, 48, 48, 38, 48, 48, 48, 48, 48, 48, 48, 48, 48, 48, 48, 48, 38, 49, 50, 51, 52, 53, 54, 55, 56, 57, 48, 49, 50, 51, 52, 53, 54, 35, 146, 126]		


print(check_command(l))


7e 02 00 00 52 01 00 36 52 64 47 51 47 00 00 00 00 00 00 00 00 01 5a 31 92 06 c8 6b a0 00 00 00 00 00 00 19 03 19 12 16 08 33 34 2a 4d 30 30 2c 34 33 2c 31 31 34 32 30 30 30 31 32 33 34 35 36 26 30 30 30 30 30 30 30 30 30 30 30 30 26 31 32 33 34 35 36 37 38 39 30 31 32 33 34 35 36 23 81 7e