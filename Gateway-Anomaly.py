#===============Server==========================================================================
import socket
import ast
import hashlib
import time
import csv
from Crypto.Util.Padding import pad, unpad
from Crypto.Cipher import AES 
from Crypto.Cipher import AES
from _thread import *
from datetime import datetime 
import pandas as pd
import numpy as np
import seaborn
from sklearn import preprocessing
from sklearn.preprocessing import StandardScaler
from sklearn import svm
from sklearn.model_selection import train_test_split
from sklearn import metrics
list_clients=[]
f= open("datalog-22Feb.csv","w")
writer = csv.DictWriter(
    f, fieldnames=["Source IP","Destination IP","Sent Time","Received Time","Node ID","Temperature","Humidity","Light","Sound","PIR","Distance","Lidar Distance","Vibration","Microwave","Size"])
f.close()
#==========================Machine Learning Model for Data anomaly==============================
df = pd.read_csv("anomaly.csv")
y = df['anomaly3']
data = df[['Temp','Light','Sound','PIR','Distance']]
X_train, X_test,y_train,y_test = train_test_split(data,y,test_size=0.2,shuffle=True)
model = svm.SVC()
y=model.fit(X_train.values,y_train)
#===============Gateway===========================================================================
UDP_IP = "10.42.0.1"
UDP_PORT = 5006
ThreadCount = 0
BLOCK_SIZE = 32
global todata,invalidIP
global connection
c= AES.new('This is a key123'.encode("utf8"), AES.MODE_CBC, 'This is an IV456'.encode("utf8"))
c1= AES.new('This is a key123'.encode("utf8"), AES.MODE_CBC, 'This is an IV456'.encode("utf8"))
sock = socket.socket(socket.AF_INET, # Internet
                  socket.SOCK_DGRAM) # UDP
sock.bind((UDP_IP, UDP_PORT)) #Zigbee Coordinator bind
ServerSocket = socket.socket()
ServerSocket.bind(('10.42.0.1', 5008))
ServerSocket.listen(5)
#print('Connected to: ' + address[0] + ':' + str(address[1]))
#=====================Zigbee Athentication =============================
def Device_athentication(Device_id,Rkey):
    global connection
    with open('skey.txt') as f:
    	tabledata = f.read()
    hashtable= ast.literal_eval(tabledata)
    sk=hashtable[Device_id]
    str1 = str (Device_id)+str(sk)
    result = hashlib.sha256(str1.encode())
    hashkey=result.hexdigest()
    'print(hashkey)'
    if Rkey==hashkey:
        #print("Authorised Coordinator:"+Device_id)
        return 1
    else:
        message="UnAuthorised Device"
	#connection.sendall(str.encode(message))
        return 0
#=====================PDA Athentication =============================
def client_athentication(mac,connection):
	#global connection
	try:
		sk=""
		with open('skey.txt') as f:
			tabledata = f.read()
		hashtable= ast.literal_eval(tabledata)
		sk=hashtable[mac]
		#print(sk)
		connection.send(sk.encode('utf-8'))
		mackey= connection.recv(2048)
		mackey=mackey.decode('utf-8')
		mac=mac+sk
		result=hashlib.sha256(mac.encode())
		mackeyGen=result.hexdigest()
	except KeyError:
		return "Invalid MAC"
	if mackey==mackeyGen:
		sts="Authorised Device"
		connection.send(sts.encode('utf-8'))
		return "Success"
	else:
		return "Invalid Key"
#=====================PDA Conncetion===============================
def NewConnection(ServerSocket):
	
	Client, address = ServerSocket.accept()
	
	start_new_thread(threaded_client, (Client,address ))
	
def threaded_client(connection,address):
	#clients.send(todata.encode('utf-8'))
	requestinfo = connection.recv(2048)
	request=requestinfo.decode('utf-8')
	requestdata=str(request).split(',',1)
	print(address)
	print(requestdata)
	status=client_athentication(requestdata[0],connection)
	now = datetime.now()
	current_time = now.strftime("%H:%M:%S")
	date=now.strftime("%b-%d-%Y")
#======================PDA Login Log=======================================================================	 	
	if status=="Success":
		msg='New Device'
		list_clients.append(connection)			
		msg= c1.encrypt(pad(msg.encode('ISO-8859-1'),32))
		print(connection)
		connection.sendall(msg)
		print("New Connection")
		f= open("Login_Log1.csv","a+")
		f.write(address[0]+","+"192.168.225.171"+","+str(address[1])+","+"5006"+","+requestdata[0]+","+date+","+current_time+","+"Active"+","+status+"\n")
		f.close()
		try:
			while True:
				global todata
				connection.sendall(todata)
				#connection.sendall(msg)
				print("data sent:",todata)
				time.sleep(1.5)
		except socket.error:
			requestinfo = connection.recv(2048)
			logoutdata=str(requestinfo).split(',',2)
			#print(connection)
			print(logoutdata[1])
			with open('Login_Log1.csv') as f:
				w=csv.writer(f)
				data=[row for row in csv.reader(f)]
				length=len(data)
				for i in range(length-1):
					i=i+1
					if data[i][0]==logoutdata[1]:
						if data[i][7]=="Active":
							data[i][7]=logoutdata[0]
							with open('Login_Log1.csv',"w") as f:
								w=csv.writer(f)
								for row in data:
									w.writerow(row)
					
								
				
			print("Connection Closed")
			
	else:
		invalidIP=address[0]
		cnt=1
		with open('Login_Log1.csv') as f:
			w=csv.writer(f)
			data=[row for row in csv.reader(f)]
			length=len(data)
			for i in range(length-1):
				i=i+1
				if data[i][0]==invalidIP:
					if data[i][8]!="Success":
						cnt=cnt+1

		print(invalidIP)
		count=str(cnt)
		print(cnt)
		f= open("Login_Log1.csv","a+")
		f.write(address[0]+","+"192.168.225.171"+","+str(address[1])+","+"5006"+","+requestdata[0]+","+date+","+current_time+","+count+","+status+"\n")
		f.close()
		connection.close()
def brodcast(message,connection):
	for clients in list_clients:
		try:
			if clients!=connection:
				clients.send(message)
				print("send")
		except socket.error:
			requestinfo = connection.recv(2048)
			logoutdata=str(requestinfo).split(',',2)
#=======================Zigbee Data Receiving==========================	
while True:
   global todata
   data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
   now = datetime.now()
   current_time = now.strftime("%Y-%m-%d:%H:%M:%S")
   #data=data.decode('utf-8')
   #print(data)
   msg_dec = c.decrypt(data)
   packet=unpad(msg_dec, BLOCK_SIZE)
   data1=packet.decode('ISO-8859-1')
   print(packet)
   #packet=packet.decode('ISO-8859-1')
   #print("received message: %s" % data.decode('utf-8'))
   datalist=str(data1).split(',',14)
   length=len(datalist)
   #print(length)
   #print(datalist)
   if length==15:
	   C_id=datalist[0]
	   hkey=datalist[1]
	   f= open("datalog-22Feb.csv","a+")
	   f.write(addr[0]+","+UDP_IP+","+datalist[14]+","+current_time+","+datalist[2]+","+datalist[3]+","+datalist[4]+","+datalist[5]+","+datalist[6]+","+datalist[7]+","+datalist[8]+","+datalist[9]+","+datalist[10]+","+datalist[11]+","+str(length)+"B"+"\n")
	   f.close()
	   livedata=[[datalist[3],datalist[5],datalist[6],datalist[7],datalist[8]]]
	   y=model.predict(livedata)
	   
	   if(datalist[7]=='1'):
	   	print("Anomaly Detected")
	   	alert="Anomaly Detected in Node:"+datalist[2]
	   else:
	   	alert="Authorised Data"
	   todata="Node:"+datalist[2]+",Temperature:"+datalist[3]+",Humidity:"+datalist[4]+",Light:"+datalist[5]+",Sound:"+datalist[6]
	   todata=todata+",PIR:"+datalist[7]+",Distance:"+datalist[8]+",Lidar Distance:"+datalist[9]+",Vibration:"+datalist[10]+",Microwave:"+datalist[11]+","+alert
	   todata= c1.encrypt(pad(todata.encode('ISO-8859-1'),32))
	   #print(current_time)
	   #print(todata)
	   status=Device_athentication(C_id,hkey)
	   if status==1:
	   	start_new_thread(NewConnection,(ServerSocket,))
ServerSocket.close()

