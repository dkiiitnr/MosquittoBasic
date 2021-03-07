import paho.mqtt.client as mqtt
import time
import pandas as pd
import os

# Taking the variables for the methods
client = mqtt.Client("Data Logger")
topicName = "unbox/frame_to_aggregator"
QOS_val = 2
global counter
i = 0

node_0 = []
node_1 = []
node_2 = []
node_3 = []

new_node_0 = []
new_node_1 = []
new_node_2 = []
new_node_3 = []

save_list_0 = []
save_list_1 = []
save_list_2 = []
save_list_3 = []


def on_connect(pvtClient, userdata, flags, rc):
    if rc == 0:
        print("Connected to client! Return Code:" + str(rc))
        result = client.subscribe(topicName, QOS_val)
    elif rc == 5:
        print("Authentication Error! Return Code: " + str(rc))
        client.disconnect()


def on_message(pvtClient, userdata, msg):
    if (msg.payload.decode()[13] == "0"):
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
        node_0 = [int(dest_id), int(pincode), int(dest_mode), int(parcel_status), int(stop_switch),
                  int(emergency_switch), int(bag_presence), int(bag_position)]
        new_node_0.append(node_0)
        print('Node 0')



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
        node_1 = [int(dest_id), int(pincode), int(dest_mode), int(parcel_status), int(stop_switch),
                  int(emergency_switch), int(bag_presence), int(bag_position)]
        new_node_1.append(node_1)
        print('Node 1')



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
        node_2 = [int(dest_id), int(pincode), int(dest_mode), int(parcel_status), int(stop_switch),
                  int(emergency_switch), int(bag_presence), int(bag_position)]
        new_node_2.append(node_2)
        print('Node 2')

    elif (msg.payload.decode()[13] == "3"):
        global i, list_compare
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
        node_3 = [int(dest_id), int(pincode), int(dest_mode), int(parcel_status), int(stop_switch),
                  int(emergency_switch), int(bag_presence), int(bag_position)]
        new_node_3.append(node_3)

        print('dest_id: ', dest_id)
        print('pincode: ', pincode)
        print('dest_mode: ', dest_mode)
        print('parcel_status: ', parcel_status)
        print('bag_presence: ', bag_presence)
        print('bag_position: ', bag_position)
        print('stop_switch: ', stop_switch)
        print('emergency_switch', emergency_switch)
        if not (new_node_3[i] == new_node_3[i - 1]):
            print(new_node_3[i])
            save_list_3.append(new_node_3[i])
        i += 1

    if msg.payload.decode() == "exit(0)":
        client.disconnect()


def save_data():
    first_node = pd.DataFrame(save_list_0,
                              columns=["Dest_ID", 'PINCODE', 'Dest_mode', 'Parcel', 'stop_switch', 'emergency_switch',
                                       'bag_presence', 'bag_position'])
    first_writer = pd.ExcelWriter('Node 1.xlsx', engine='xlsxwriter')
    first_node.to_excel(first_writer, sheet_name="Node_1")

    second_node = pd.DataFrame(save_list_1,
                               columns=["Dest_ID", 'PINCODE', 'Dest_mode', 'Parcel', 'stop_switch', 'emergency_switch',
                                        'bag_presence', 'bag_position'])
    second_writer = pd.ExcelWriter('Node 2.xlsx', engine='xlsxwriter')
    second_node.to_excel(second_writer, sheet_name="Node_2")

    third_node = pd.DataFrame(save_list_2,
                              columns=["Dest_ID", 'PINCODE', 'Dest_mode', 'Parcel', 'stop_switch', 'emergency_switch',
                                       'bag_presence', 'bag_position'])
    third_writer = pd.ExcelWriter('Node 3.xlsx', engine='xlsxwriter')
    third_node.to_excel(third_writer, sheet_name="Node_3")

    fourth_node = pd.DataFrame(save_list_3,
                               columns=["Dest_ID", 'PINCODE', 'Dest_mode', 'Parcel', 'stop_switch', 'emergency_switch',
                                        'bag_presence', 'bag_position'])
    fourth_writer = pd.ExcelWriter('Node 4.xlsx', engine='xlsxwriter')
    fourth_node.to_excel(fourth_writer, sheet_name="Node_4")


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
    try:
        main()
    except:
        save_data()
