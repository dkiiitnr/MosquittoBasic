import paho.mqtt.client as paho
import sys
def on_message (clinet,userdata,msg):
    print(msg.topic + " : " + msg.payload.decode("UTF-8"))

client = paho.Client()
client.on_message =on_message
# if client.connect("localhost",1883,60)!=0
if client.connect("localhost",1883,30) !=0:
    print("could not connect to mqtt broker")
    sys.exit(-1)


client.subscribe("topic")
try:
    print("Press exit")
    client.loop_forever()
except:
    print("Disconnecting from broker")

client.disconnect()

