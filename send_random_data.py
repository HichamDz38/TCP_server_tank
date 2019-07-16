import random
import time
import requests
import sys
site=sys.argv[1]
devices=['044040906889', '044040900726','044040897641','044040890646','044040891339', '044040895520','044040897351','070048196884','044040890596','044040894051','044040896577']
while True:
	data={
		'Terminal_ID':random.choice(devices),
		'alert':random.randint(0,4294967295),
		'status':random.randint(0,4294967295),
		'latitude':random.randrange(0,90)+random.random(),
		'longitude':random.randrange(0,180)+random.random(),
		'length':random.randrange(0,100),
		'speed':random.randrange(0,100),
		'direction':random.randrange(0,100),
		'time':time.strftime('%Y-%m-%d %H:%I:%S'),
		"Lock_status":random.choice([0,1]),
		"Seal_status":random.choice([0,1]),
		"Battery":random.randrange(0,400),
		"Tamper_status":random.choice([0,1]),
		"Repport_reason":random.choice('0123456789ABCDEFGHIJKLMNOPQRST'),
		"Operational_ID":random.choice(devices),
		"Sub_lock_state":random.choice("0000012345")+random.choice("0000012345")+random.choice("010000345")+random.choice("0123000045")+random.choice("0123000045")+random.choice("0123000045")+random.choice("0120000345")+random.choice("0120000405")+random.choice("012300045")+random.choice("0000012345")+random.choice("0000012345")+random.choice("0000012345"),
		"User_busness_ID":random.choice(devices),
		'Milage':random.randrange(0,400),
		'Oil_qualtity':random.randrange(0,400),	}
	print(data['Terminal_ID'],data['latitude'],data['longitude'])
	#time.sleep(0.1)
	r = requests.post(site,data)
	#print("send data")
	#print(site,data)
	#print(r.text,r.status_code)
	if r.status_code!=200:
		print(error)
	print( r.text)