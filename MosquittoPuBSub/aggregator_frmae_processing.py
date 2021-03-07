import sys 
import random
import numpy
import pandas as pd
# from frame_creation  import rack_frame 


#bag status is not cheked in active pause mode 
#also parcel dumped successfully is error in active pause,deactivate and stop 


def emergency_callback():
	mode = "emergency"
	error = "Emergency has arravied"
	update_log_file(mode, error)
	stop()

def stop():
	sys.exit()

def stop_callback():
	mode = "stop"
	check_parcel_status(mode)

def check_emergency_switch(emergency_switch, mode):
	if emergency_switch == "pressed" or mode == "emergency":
		emergency_callback()
	else:
		check_manual_stop_switch(mode)

def check_manual_stop_switch(mode):
	if stop_manual_switch == "pressed" or mode == "stop":
		stop_callback()
	elif mode == "deactivate":
		check_parcel_status(mode)
	else:
		check_destination_position()

def check_destination_position():
	if destintion_position == "AGV_Mode":
		check_bag_status()
	else:
		mode = "active_pause"
		check_parcel_status(mode)

def check_bag_status():
	if bag_status == "present":
		mode = "active_start"
		print(f"mode is {mode}")
	else:
		mode = "active_pause"
		print(f"mode is {mode}")
	check_parcel_status(mode)

def check_parcel_status(mode):
	global error
	if parcel_status == "dumped successfully":
		if mode == "active_pause" or mode == "deactivate" or mode =="stop":
			error = "Parcel Should not Show in This Mode"
			update_log_file(mode, error)
		else:
			mode = "active_start"
			error = "None"
			update_log_file(mode, error)
	elif parcel_status == "ready to receive":
		error = "None"
		update_log_file(mode, error)
	else:
		error = "Parcel Is Stuck at Destination"
		update_log_file(mode,error)
	

def update_log_file(mode, error):
	
	data = {'Mode': [mode], 'Emergency Switch': [emergency_switch],
			'Stop Switch': [stop_manual_switch], 'Destintion_Position'
			'Bag Status': [bag_status], 'Parcel Status': [parcel_status], 'Error': [error]}
	Output_frame = pd.DataFrame(data, columns = ['Mode', 'Emergency_switch', 'Stop switch', 'Destintion_Position', 'Bag Status', 'Parcel Status', 'Error'])

	writer = pd.ExcelWriter('Output.xlsx', engine='xlsxwriter')
	Output_frame.to_excel(writer, sheet_name='Log File')
	# writer.save()
	print(Output_frame)

def main():
	global mode, bag_status, parcel_status, emergency_switch,stop_manual_switch, destintion_position
	mode = input("Enter Rack Mode: ")
	emergency_switch = input("Enter Emergency_switch: ")
	stop_manual_switch = input("Enter Stop Switch: ")
	destintion_position = input("Enter Destintion_Position: ")
	bag_status = input("Enter bag_status: ")
	parcel_status =  input("Enter parcel_status: ")

	data = {'Mode': [mode], 'Emergency Switch': [emergency_switch],
			'Stop Switch': [stop_manual_switch], 'Destintion_Position'
			'Bag Status': [bag_status], 'Parcel Status': [parcel_status]}
	input_frame = pd.DataFrame(data, columns = ['Mode', 'Emergency_switch', 'Stop switch', 'Destintion_Position', 'Bag Status', 'Parcel Status'])
	
	print((mode) + str(" ") + (emergency_switch)+ str(" ") + (stop_manual_switch) + str(" ") + (destintion_position) + str(" ") + (bag_status) + str(" ") + (parcel_status))
	writer = pd.ExcelWriter('Input.xlsx', engine='xlsxwriter')
	input_frame.to_excel(writer, sheet_name='Log File')
	# writer.save()

	print(input_frame)
	if mode :
		check_emergency_switch(emergency_switch, mode)
	else:
		print("Nothing")
	

if __name__ == '__main__':
	main()