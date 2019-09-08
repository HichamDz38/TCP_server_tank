import time
import mysql.connector
def insert_data(D):
	mydb=mysql.connector.connect(
		host="localhost",
		user="root",
		passwd="ST#hwh@Ac@21",
		database="tank"
	)

	mycursor=mydb.cursor()
	mycursor.execute("select id from devices where sn="+D[0])
	r=mycursor.fetchall()
	if not r:
		return False
	_id=str(r[0][0])
	#D[1],D[2],D[3]=str(D[1]),str(D[2]),str(D[3])
	T=D[4]
	D=list(map(str,D))
	mycursor.execute("insert into data(id_device,Latitude,Longitude,oil_quantity,date,speed,angle,gps_status,detection_setting,ignition_status,oil_resistance) values ('"+_id+"','"+D[1]+"','"+D[2]+"','"+D[3]+"','"+T+"','"+D[5]+"','"+D[6]+"','"+D[7]+"','"+D[8]+"','"+D[9]+"','"+D[10]+"')")
	mydb.commit()
	print(mycursor.rowcount, "record inserted.")