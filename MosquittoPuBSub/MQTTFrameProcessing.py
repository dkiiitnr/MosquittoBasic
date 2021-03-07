import paho.mqtt.client as mqtt
import time
import pandas as pd
import sys
from frame_creation import Rack
from MQTTPublisher import Publisher

'''This is main frame processing unit which subscribes to data coming from NodeMCU and based on receieved frame it 
prepares new python list of data and then sends the frame to frame_creation to convert into string and then performs 
aggregator logic and returns required this to send back to NodeMCU'''

sys.path.append(".")  # python Path

# Taking the variables for the methods
client = mqtt.Client("Frame Processor")
# topic to Receive Data
topicName = "unbox/frame_to_aggregator"
# topic to Send Data
topic_to_arduino = "unbox/frame_to_dest"
QOS_val = 0


def on_connect(pvtClient, userdata, flags, rc):
    if rc == 0:
        print("Connected to client! Return Code:" + str(rc))
        result = client.subscribe(topicName, QOS_val)  # Subscribing to Conroller Data
    elif rc == 5:
        print("Authentication Error! Return Code: " + str(rc))
        client.disconnect()


def on_message(pvtClient, userdata, msg):
    if msg.payload.decode()[13] == "0":  # The Last array Element decides Controller address.later change to
        # Wifi.LocalIP() at NodeMCU
        dest_id = msg.payload.decode()[0]
        pincode = msg.payload.decode()[1]
        pincode += msg.payload.decode()[2]
        pincode += msg.payload.decode()[3]
        pincode += msg.payload.decode()[4]
        pincode += msg.payload.decode()[5]
        pincode += msg.payload.decode()[6]
        dest_mode = msg.payload.decode()[7]
        parcel_status = msg.payload.decode()[8]
        stop_switch = msg.payload.decode()[9]
        emergency_switch = msg.payload.decode()[10]
        bag_position = msg.payload.decode()[11]
        bag_presence = msg.payload.decode()[12]
        hey = Rack(dest_id, int(dest_mode), int(emergency_switch), int(stop_switch), int(bag_position),
                   int(bag_presence), int(parcel_status))
        frame_dest_mode = hey.assign_mode()  # converting Int into String for processing
        frame_parcel_status = hey.assign_parcel_status()  # converting Int into String for processing
        frame_bag_presence = hey.assign_bag_presence()  # converting Int into String for processing
        frame_stop_switch = hey.assign_stop_switch()  # converting Int into String for processing
        frame_emergency_switch = hey.assign_e_switch()  # converting Int into String for processing
        frame_destination_position = hey.assign_destination_position()  # converting Int into String for processing
        hey.check_emergency_switch(frame_emergency_switch, frame_dest_mode)  # Initiating Frame processing from
        # Emergency Checking
        new_id, new_mode, error = hey.return_state()  # Getting Information From Aggregator Logic (this is String)
        frame_to_publish = Publisher(new_id, new_mode, error)  # Instantiating Publisher from MQTTPublisher Class
        new_id, new_mode, error = frame_to_publish.return_int()  # Converting String back to int to send to controller
        print("dest_id:", new_id)
        print("dest_mode: ", new_mode)
        print("error: ", error)
        payload = str(new_id) + str(new_mode) + str(error)
        client.publish(topic_to_arduino, payload)  # Publishing data to Controller



    elif (msg.payload.decode()[13] == "1"):
        dest_id = msg.payload.decode()[0]
        pincode = msg.payload.decode()[1]
        pincode += msg.payload.decode()[2]
        pincode += msg.payload.decode()[3]
        pincode += msg.payload.decode()[4]
        pincode += msg.payload.decode()[5]
        pincode += msg.payload.decode()[6]
        dest_mode = msg.payload.decode()[7]
        parcel_status = msg.payload.decode()[8]
        stop_switch = msg.payload.decode()[9]
        emergency_switch = msg.payload.decode()[10]
        bag_position = msg.payload.decode()[11]
        bag_presence = msg.payload.decode()[12]
        hey = Rack(dest_id, int(dest_mode), int(emergency_switch), int(stop_switch), int(bag_position),
                   int(bag_presence), int(parcel_status))
        frame_dest_mode = hey.assign_mode()  # converting Int into String for processing
        frame_parcel_status = hey.assign_parcel_status()  # converting Int into String for processing
        frame_bag_presence = hey.assign_bag_presence()  # converting Int into String for processing
        frame_stop_switch = hey.assign_stop_switch()  # converting Int into String for processing
        frame_emergency_switch = hey.assign_e_switch()  # converting Int into String for processing
        frame_destination_position = hey.assign_destination_position()  # converting Int into String for processing
        hey.check_emergency_switch(frame_emergency_switch, frame_dest_mode)  # Initiating Frame processing from
        # Emergency Checking
        new_id, new_mode, error = hey.return_state()  # Getting Information From Aggregator Logic (this is String)
        frame_to_publish = Publisher(new_id, new_mode, error)  # Instantiating Publisher from MQTTPublisher Class
        new_id, new_mode, error = frame_to_publish.return_int()  # Converting String back to int to send to controller
        print("dest_id:", new_id)
        print("dest_mode: ", new_mode)
        print("error: ", error)
        payload = str(new_id) + str(new_mode) + str(error)
        client.publish(topic_to_arduino, payload)  # Publishing data to Controller




    elif (msg.payload.decode()[13] == "2"):
        dest_id = msg.payload.decode()[0]
        pincode = msg.payload.decode()[1]
        pincode += msg.payload.decode()[2]
        pincode += msg.payload.decode()[3]
        pincode += msg.payload.decode()[4]
        pincode += msg.payload.decode()[5]
        pincode += msg.payload.decode()[6]
        dest_mode = msg.payload.decode()[7]
        parcel_status = msg.payload.decode()[8]
        stop_switch = msg.payload.decode()[9]
        emergency_switch = msg.payload.decode()[10]
        bag_position = msg.payload.decode()[11]
        bag_presence = msg.payload.decode()[12]
        hey = Rack(dest_id, int(dest_mode), int(emergency_switch), int(stop_switch), int(bag_position),
                   int(bag_presence), int(parcel_status))
        frame_dest_mode = hey.assign_mode()  # converting Int into String for processing
        frame_parcel_status = hey.assign_parcel_status()  # converting Int into String for processing
        frame_bag_presence = hey.assign_bag_presence()  # converting Int into String for processing
        frame_stop_switch = hey.assign_stop_switch()  # converting Int into String for processing
        frame_emergency_switch = hey.assign_e_switch()  # converting Int into String for processing
        frame_destination_position = hey.assign_destination_position()  # converting Int into String for processing
        hey.check_emergency_switch(frame_emergency_switch, frame_dest_mode)  # Initiating Frame processing from
        # Emergency Checking
        new_id, new_mode, error = hey.return_state()  # Getting Information From Aggregator Logic (this is String)
        frame_to_publish = Publisher(new_id, new_mode, error)  # Instantiating Publisher from MQTTPublisher Class
        new_id, new_mode, error = frame_to_publish.return_int()  # Converting String back to int to send to controller
        print("dest_id:", new_id)
        print("dest_mode: ", new_mode)
        print("error: ", error)
        payload = str(new_id) + str(new_mode) + str(error)
        client.publish(topic_to_arduino, payload)  # Publishing data to Controller


    elif (msg.payload.decode()[13] == "3"):
        dest_id = msg.payload.decode()[0]
        pincode = msg.payload.decode()[1]
        pincode += msg.payload.decode()[2]
        pincode += msg.payload.decode()[3]
        pincode += msg.payload.decode()[4]
        pincode += msg.payload.decode()[5]
        pincode += msg.payload.decode()[6]
        dest_mode = msg.payload.decode()[7]
        parcel_status = msg.payload.decode()[8]
        stop_switch = msg.payload.decode()[9]
        emergency_switch = msg.payload.decode()[10]
        bag_position = msg.payload.decode()[11]
        bag_presence = msg.payload.decode()[12]
        print('', dest_id, dest_mode, emergency_switch, stop_switch, bag_position, bag_presence, parcel_status)
        # hey is class object of Rack which is imported from frame_creation
        hey = Rack(dest_id, int(dest_mode), int(emergency_switch), int(stop_switch), int(bag_position),
                   int(bag_presence), int(parcel_status))
        frame_dest_mode = hey.assign_mode()  # converting Int into String for processing
        frame_parcel_status = hey.assign_parcel_status()  # converting Int into String for processing
        frame_bag_presence = hey.assign_bag_presence()  # converting Int into String for processing
        frame_stop_switch = hey.assign_stop_switch()  # converting Int into String for processing
        frame_emergency_switch = hey.assign_e_switch()  # converting Int into String for processing
        frame_destination_position = hey.assign_destination_position()  # converting Int into String for processing
        hey.check_emergency_switch(frame_emergency_switch, frame_dest_mode)  # Initiating Frame processing from
        # Emergency Checking
        new_id, new_mode, error = hey.return_state()  # Getting Information From Aggregator Logic (this is String)
        frame_to_publish = Publisher(new_id, new_mode, error)  # Instantiating Publisher from MQTTPublisher Class
        new_id, new_mode, error = frame_to_publish.return_int()  # Converting String back to int to send to controller
        print("dest_id:", new_id)
        print("dest_mode: ", new_mode)
        print("error: ", error)
        payload = str(new_id) + str(new_mode) + str(error)
        client.publish(topic_to_arduino, payload)  # Publishing data to Controller

    if msg.payload.decode() == "exit(0)":
        client.disconnect()


def main():
    client.on_connect = on_connect
    client.on_message = on_message
    # client.on_disconnect = on_disconnect
    host = "localhost"
    port = 1883
    keepAlive = 60

    client.connect(host, port, keepAlive)  # establishing the connection

    time.sleep(1)  # giving a sleep time for the connection to setup

    client.loop_forever()


if __name__ == '__main__':
    main()
