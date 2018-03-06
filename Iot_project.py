import bluetooth
import serial
import time
import urllib.request
import json
import re
import pyodbc


dsn = 'yourdsnname' #Put your DSN name
server = 'yourservername' #server name
user = 'username' #User name
password = 'password' #password
database = 'DBname' #DB to access
cnsn = pyodbc.connect('DSN=%s;UID=%s;PWD=%s;DATABASE=%s;'%(dsn,user,password,database))
cursor = cnsn.cursor()

bd_addr = "macAddress" #The address from the HC–05 sensor
port = 1
sock = bluetooth.BluetoothSocket (bluetooth.RFCOMM)
sock.connect((bd_addr,port))
data1 = ""
time.sleep(5)
name = ['rainValue','humidity','temperature']



while 1:
    data_end=0
    try:
        data1 += sock.recv(1024).decode('UTF-8', 'ignore')
        data_end = data1.find('\n')

        if data_end != -1:
            rec=data1[:data_end]
            data2 = data1.split(",")
            print("--------------------------")
            if data1!="1":

                data = {
                        "Inputs": {
                                "input1":
                                [
                                    {
                                            'temperature': data2[2],
                                            'humidity': data2[1],
                                    }
                                ],
                        },
                    "GlobalParameters":  {
                    }
                }

                body = str.encode(json.dumps(data))
                # send Information to our  Azure ML service app
                url = 'YourWebAppURL' #Replace this with the WebApp URL
                api_key = 'YourWebServiceAPIkey' # Replace this with the API key for the web service
                headers = {'Content-Type':'application/json', 'Authorization':('Bearer '+ api_key)}

                req = urllib.request.Request(url, body, headers)

                try:
                    response = urllib.request.urlopen(req)

                    result = response.read()
                    result1 = result.decode("utf-8")
                    result2 = result1.split(",")
                    result3 = result2[3].split('"')
                    result_f = result3[3]

                    print(result_f)
                    time.sleep(3)

                except urllib.error.HTTPError as error:
                    print("The request failed with status code: " + str(error.code))

                    # Print the headers - they include the requert ID and the timestamp, which are useful for debugging the failure
                    print(error.info())
                    print(json.loads(error.read().decode("utf8", 'ignore')))





                for i in range(0,3):
                    print(i)
                    n = name[i]
                    d = data2[i]
                    print("n: "+n)
                    print("d: "+d)

                    insert = ("INSERT INTO [dbo].[iotnice]([sensor],[sensorValue],[probabilities],[date]) VALUES (?,?,?,CONVERT(DATETIME,SYSDATETIMEOFFSET() AT TIME ZONE 'China Standard Time'))")
                    value = (n,d,result_f)
                    cursor.execute(insert,value)
                    cnsn.commit()



                #put = ("INSERT INTO [dbo].[iotnice]([probabilities]) VALUES (?)")
                #value1 = (result_f)
                #cursor.execute(put,value1)
                #cnsn.commit()
                data1 = data1[data_end+1:]
                time.sleep(0.5)



    except KeyboardInterrupt:
        break

sock.close()
