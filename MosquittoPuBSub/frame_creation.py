import numpy
import pandas as pd
import os
import sys

'''this class is instantiated from MQTTFrameProcessing. it receives integers from MQTTFrameProcessor Subscriber 
converts them into string for processing based on frame it starts verifying it from check emergency and the logic is 
followed from Aggregator Rack Logic diagrame. after processing frame it saves the response frame into a log file and 
then returns string of dest_id, dest_mode, and error. we can return other elements as well'''


class Rack:

    def __init__(self, dest_id, mode, emergency_switch, stop_switch, destination_position, bag_presence, parcel_status):

        self.dest_id = dest_id
        self.mode = mode
        self.emergency_switch = emergency_switch
        self.stop_switch = stop_switch
        self.destination_position = destination_position
        self.bag_presence = bag_presence
        self.parcel_status = parcel_status
        self.error = ""
        self.bag_status = self.bag_presence
        self.stop_manual_switch = self.stop_switch

    def assign_mode(self):
        if self.mode == 1:
            self.mode = "active_start"
        elif self.mode == 2:
            self.mode = "active_pause"
        elif self.mode == 3:
            self.mode = "deactivate"
        elif self.mode == 4:
            self.mode = "stop"
        else:
            self.mode = "emergency"
        return self.mode

    def assign_e_switch(self):
        if self.emergency_switch == 1:
            self.emergency_switch = "pressed"
        else:
            self.emergency_switch = "not_pressed"
        return self.emergency_switch

    def assign_stop_switch(self):
        if self.stop_switch == 1:
            self.stop_switch = "pressed"
        else:
            self.stop_switch = "not_pressed"
        return self.stop_switch

    def assign_destination_position(self):
        if self.destination_position == 1:
            self.destination_position = "AGV_Mode"
        else:
            self.destination_position = "Manual_mode"
        return self.destination_position

    def assign_bag_presence(self):
        if self.bag_presence == 1:
            self.bag_presence = "present"
        else:
            self.bag_presence = "absent"
        return self.bag_presence

    def assign_parcel_status(self):
        if self.parcel_status == 1:
            self.parcel_status = "dumped successfully"
        else:
            self.parcel_status = "parcel_stuck"
        return self.parcel_status

    def emergency_callback(self):
        self.mode = "emergency"
        self.error = "Emergency has arrived"
        self.update_log_file(self.mode, self.error)
        self.stop()

    def stop(self):
        print('Stopping due to emergency')
        # sys.exit()

    def stop_callback(self):
        self.mode = "stop"
        self.check_parcel_status(self.mode)

    def check_emergency_switch(self, emergency_switch, mode):
        if self.emergency_switch == "pressed" or self.mode == "emergency":
            self.emergency_callback()
        else:
            self.check_manual_stop_switch(self.mode)

    def check_manual_stop_switch(self, mode):
        if self.stop_manual_switch == "pressed" or self.mode == "stop":
            self.stop_callback()
        elif self.mode == "deactivate":
            self.check_parcel_status(mode)
        else:
            self.check_destination_position()

    def check_destination_position(self):
        if self.destination_position == "AGV_Mode":
            self.check_bag_status()
        else:
            self.mode = "active_pause"
            self.check_parcel_status(self.mode)

    def check_bag_status(self):
        if self.bag_presence == "present":
            self.mode = "active_start"
            print(f"mode is {self.mode}")
        else:
            self.error = "Bag is absent"
            self.mode = "active_pause"
            print(f"mode is {self.mode}")
        self.check_parcel_status(self.mode)

    def check_parcel_status(self, mode):
        if self.parcel_status == "dumped successfully":
            if self.mode == "active_pause" or self.mode == "deactivate" or self.mode == "stop":
                self.error = "Parcel Should not Show in This Mode"
                self.update_log_file(self.mode, self.error)
            else:
                self.mode = "active_start"
                self.error = "None"
                self.update_log_file(self.mode, self.error)
        elif self.parcel_status == "ready to receive":
            self.error = "None"
            self.update_log_file(mode, self.error)

        else:
            self.error = "Parcel Is Stuck at Destination"
            self.update_log_file(self.mode, self.error)

    def update_log_file(self, mode, error):
        self.data = {'Mode': [self.mode], 'Emergency Switch': [self.emergency_switch],
                     'Stop Switch': [self.stop_manual_switch], 'Destintion_Position'
                                                               'Bag Status': [self.bag_presence],
                     'Parcel Status': [self.parcel_status],
                     'Error': [self.error]}
        self.Output_frame = pd.DataFrame(self.data,
                                         columns=['Mode', 'Emergency_switch', 'Stop switch', 'Destintion_Position',
                                                  'Bag Status',
                                                  'Parcel Status', 'Error'])

        writer = pd.ExcelWriter('Output.xlsx', engine='xlsxwriter')
        self.Output_frame.to_excel(writer, sheet_name='Log File')
        writer.save()

    def return_state(self):
        return self.dest_id, self.mode, self.error


def main():
    check_frame = Rack(3, 1, 0, 0, 1, 1, 0)
    mode = check_frame.assign_mode()
    emergency_switch = check_frame.assign_e_switch()
    stop_switch = check_frame.assign_stop_switch()
    destination_position = check_frame.assign_destination_position()
    bag_presence = check_frame.assign_bag_presence()
    parcel_status = check_frame.assign_parcel_status()
    print(mode, emergency_switch, stop_switch, destination_position, bag_presence, parcel_status)
    check_frame.check_emergency_switch(emergency_switch, mode)
    state = check_frame.return_state()
    print(state)


if __name__ == "__main__":
    main()
