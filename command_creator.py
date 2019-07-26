# -*- coding: utf-8 -*-
import time


def Rollcall(IP):
	ip=list(map(int,IP.split(".")))
	code=0
	for i in m:
		code^=i
	M=[0x24,0x24,0x03,0x00,0x06]+[ip]+[code]+[0x0d]
	M2=list(map(lambda x:hex(x)[2:].rjust(2,'0'),M))
	print(' '.join(M2))
	print('-----------------------------------------------------------------------------')
	return M