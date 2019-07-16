# -*- coding: utf-8 -*-
import time
import requests

def send_data(data,site):
	r = requests.post(site,data)
	#print("send data")
	#print(site,data)
	#print(r.text,r.status_code)
	if r.status_code!=200:
		return 1
	return r.text

def main():
	while True:
		site=input('website   :')
		if site=='exit':
			break
		data=eval(input('enter data   :'))
		code=send_data(data,site)
		if code==0:print("Success/Confirmed")
		elif code==1:print("Failed")
		elif code==2:print("Error")
		elif code==3:print("Not Support")

def main2(site):
	while True:
		data=input('enter data   :')
		if data=='exit':
			break
		data=eval(data)
		code=send_data(data,site)
		if code==0:print("Success/Confirmed")
		elif code==1:print("Failed")
		elif code==2:print("Error")
		elif code==3:print("Not Support")



if __name__=='__main__':
	m=input("enter mode 1 or 2   :")
	if m=='1':main()
	elif m=='2':
		site=input('website   :')
		main2(site)