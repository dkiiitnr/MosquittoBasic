
import paho.mqtt.client as paho
import serial
from serial import Serial
broker="localhost"
port=1883
# global data
database= {
"RKI-2536"          :[2200, "scanner"],
str(7622201423216)  :[235,  "bournvita"],
str(261459)         :[100,  "nut"],
str(69606800395)    :[937,  "electronic comp"],
str(5060214370240)  :[4500,  "RPI"],
str(69659265885)    :[945,   "Robu.in"],
"Z36798373"         :[1500,  "Hand Sanitizer"]
}
# class Database:
#     def __init__(self,barcodeID):
#         self.barcode = barcode
#         self.name_of_item=""
#     def return_price(self):
#         return database[self.barcode][0]        

def myserial():
    ser  = serial.Serial("com11",9600)
    barcode_data = ser.readline(1000).decode("utf-8").strip()
    return barcode_data

def on_publish(client,userdata,result): 
    pass
    

def main():
    client1= paho.Client("control1")                             #create client object
    client1.on_publish = on_publish                              #assign function to callback
    client1.connect(broker,port)  
    
     
    while(True):
        print("Scan the Barcode \n")
        barcode_data = myserial()
        ret=client1.publish("topic",(database[str(barcode_data)][0]))
         

if __name__ == "__main__":
   main()
   
