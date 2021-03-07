import paho.mqtt.client as mqtt
import time
import pandas as pd

# Taking the variables for the methods
client = mqtt.Client("Deepak")
topicName = "unbox/frame_to_aggregator"
QOS_val = 2
count = 0

dest_id_0 = []
pincode_0 = []
dest_mode_0 = []
parcel_status_0 = []
bag_presence_0 = []
bag_position_0 = []
NodeMCU_0 = []

dest_id_1 = []
pincode_1 = []
dest_mode_1 = []
parcel_status_1 = []
bag_presence_1 = []
bag_position_1 = []
NodeMCU_1 = []
# client.username_pw_set(username="aman",password="youtube")

# --------------- Defining call backs---------------------------------------------------------------
def on_connect(pvtClient, userdata, flags, rc):
	if rc == 0:  # on successful connection
		print("Connected to client! Return Code:" + str(rc))  # printing the data on the screen
		# Once connection is established, subscribe to the topic
		# important, here we are subscribing to a topic only after getting the authentication done
		# further we are setting the QOS in the .subscribe(...) method
		result = client.subscribe(topicName, QOS_val)  # getting the Tuple from the call back
	elif rc == 5:  # in case of authentication error
		print("Authentication Error! Return Code: " + str(rc))  # printing the data on the screen
		client.disconnect()


#           Call back for the message
# This call-back will run whenever there is a message (payload) published on the given topic
def on_message(pvtClient, userdata, msg):
	# here we are extracting details from the msg parameter,
	# print("\n============================================")
	# print((msg.payload.decode()))
	
	# print((msg.payload.decode()[11], i+1))

	if(msg.payload.decode()[11] == "0"):
		NodeMCU_0.append(int(msg.payload.decode()))
		payload = msg.payload.decode()
		# dest_id = msg.payload.decode()[0]
		# pincode = msg.payload.decode()[1]
		# pincode += msg.payload.decode()[2]
		# pincode += msg.payload.decode()[3]
		# pincode += msg.payload.decode()[4]
		# pincode += msg.payload.decode()[5]
		# pincode += msg.payload.decode()[6]
		# dest_mode = msg.payload.decode()[7]
		# parcel_status = msg.payload.decode()[8]
		# bag_presence = msg.payload.decode()[9]
		# bag_position = msg.payload.decode()[10]
		extract_values(NodeMCU_0, 0, payload)
		# print("dest_id: ", dest_id)
		# print("pincode: ", pincode)
		# print("dest_mode: ", dest_mode)
		# print("parcel_status: ", parcel_status)
		# print("bag_presence: ", bag_presence)
		# print("bag_position: ", bag_position)
		# print("First Node:", len(NodeMCU_0))
		# write_to_excel(NodeMCU_0, 0)


	elif(msg.payload.decode()[11] == "1"):
		NodeMCU_1.append(int(msg.payload.decode()))
		dest_id = msg.payload.decode()[0]
		pincode = msg.payload.decode()[1]
		pincode += msg.payload.decode()[2]
		pincode += msg.payload.decode()[3]
		pincode += msg.payload.decode()[4]
		pincode += msg.payload.decode()[5]
		pincode += msg.payload.decode()[6]
		dest_mode = msg.payload.decode()[7]
		parcel_status = msg.payload.decode()[8]
		bag_presence = msg.payload.decode()[9]
		bag_position = msg.payload.decode()[10]

		dest_id_1.append(int(dest_id))
		pincode_1.append(int(pincode))
		dest_mode_1.append(int(dest_mode))
		parcel_status_1.append(int(parcel_status))
		bag_presence_1.append(int(bag_presence))
		bag_position_1.append(int(bag_position))


		data = {'Dest_ID' :dest_id_1,'PINCODE':pincode_1, 'Dest_mode':dest_mode_1,
				'Parcel': parcel_status_1,'bag_presence':bag_presence_1,'bag_position':bag_position_1}
		logged_data = pd.DataFrame(data, columns = ["Dest_ID", 'PINCODE', 'Dest_mode', 'Parcel', 'bag_presence', 'bag_position'])
		writer = pd.ExcelWriter('Node 2.xlsx', engine='xlsxwriter')
		logged_data.to_excel(writer, sheet_name = "Node_1")
		

	elif(msg.payload.decode()[11] == "2"):
		NodeMCU_2.append(int(msg.payload.decode()))
		dest_id = msg.payload.decode()[0]
		pincode = msg.payload.decode()[1]
		pincode += msg.payload.decode()[2]
		pincode += msg.payload.decode()[3]
		pincode += msg.payload.decode()[4]
		pincode += msg.payload.decode()[5]
		pincode += msg.payload.decode()[6]
		dest_mode = msg.payload.decode()[7]
		parcel_status = msg.payload.decode()[8]
		bag_presence = msg.payload.decode()[9]
		bag_position = msg.payload.decode()[10]
		print("dest_id: ", dest_id)
		print("pincode: ", pincode)
		print("dest_mode: ", dest_mode)
		print("parcel_status: ", parcel_status)
		print("bag_presence: ", bag_presence)
		print("bag_position: ", bag_position)
		print("Third Node:", len(NodeMCU_2))
		# NodeMCU_1.append(int(msg.payload.decode()))
		data = NodeMCU_2
		logged_data = pd.DataFrame(data, columns = ["Sub Data"])
		writer = pd.ExcelWriter('Node 3.xlsx', engine='xlsxwriter')
		logged_data.to_excel(writer, sheet_name = "Node_3")

	elif(msg.payload.decode()[11] == "3"):
		NodeMCU_3.append(int(msg.payload.decode()))
		dest_id = msg.payload.decode()[0]
		pincode = msg.payload.decode()[1]
		pincode += msg.payload.decode()[2]
		pincode += msg.payload.decode()[3]
		pincode += msg.payload.decode()[4]
		pincode += msg.payload.decode()[5]
		pincode += msg.payload.decode()[6]
		dest_mode = msg.payload.decode()[7]
		parcel_status = msg.payload.decode()[8]
		bag_presence = msg.payload.decode()[9]
		bag_position = msg.payload.decode()[10]
		print("dest_id: ", dest_id)
		print("pincode: ", pincode)
		print("dest_mode: ", dest_mode)
		print("parcel_status: ", parcel_status)
		print("bag_presence: ", bag_presence)
		print("bag_position: ", bag_position)
		print("Fourth Node:", len(NodeMCU_3))
		# NodeMCU_1.append(int(msg.payload.decode()))
		data = NodeMCU_3
		logged_data = pd.DataFrame(data, columns = ["Sub Data"])
		writer = pd.ExcelWriter('Node 3.xlsx', engine='xlsxwriter')
		logged_data.to_excel(writer, sheet_name = "Node_3")

	if msg.payload.decode() == "exit(0)":
		client.disconnect()

def print_values(node_data, node_number, msg):
	print(payload)
	
		

# ======== Associating the methods with the given callbacks of the MQTT ======
client.on_connect = on_connect
client.on_message = on_message
host = "localhost"
port = 1883
keepAlive = 60

client.connect(host, port, keepAlive)  # establishing the connection

time.sleep(1)  # giving a sleep time for the connection to setup

client.loop_forever()
# print(len(NodeMCU_0), len(NodeMCU_1))
