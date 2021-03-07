import paho.mqtt.client as mqtt
import time
import socket
import random
'''This is class used to perform string to integers'''

topic_to_arduino = "unbox/frame_to_dest"  # will only be used in case of if __name__ clause
host = "localhost"
port = 1883
keepAlive = 60

client = mqtt.Client()

exitFlag = True


class Publisher:
    def __init__(self, dest_id, dest_mode, error):
        self.dest_id = dest_id
        self.dest_mode = dest_mode
        self.error = error
        self.QOS = 0
        # self.host = "localhost"
        # self.port = 1883
        # self.keepAlive = 60

        if self.dest_mode == "active_start":
            self.dest_mode = 1
        elif self.dest_mode == "active_pause":
            self.dest_mode = 2
        elif self.dest_mode == "deactivate":
            self.dest_mode = 3
        elif self.dest_mode == "stop":
            self.dest_mode = 4
        else:
            self.dest_mode = 5

        if self.error == "Parcel Should not Show in This Mode":
            self.error = 1
        elif self.error == "Emergency has arrived":
            self.error = 2
        elif self.error == "Bag is absent":
            self.error = 3
        elif self.error == "Parcel Is Stuck at Destination":
            self.error = 4
        else:
            self.error = 0

        self.payload = str(self.dest_id) + str(self.dest_mode) + str(self.error)
        client.on_publish = self.on_publish
        client.on_connect = self.on_connect
        client.on_log = self.on_log
        client.on_disconnect = self.on_disconnect

    def on_publish(self, client, userdata, mid):
        print("Payload Published: " + str(mid))

    def on_connect(self, pvtClient, userdata, flags, rc):
        global exitFlag
        if rc == 0:
            print("publisher Connected")
            print("Connected to client! Return Code:" + str(rc))
            exitFlag = False


        elif (rc == 5):  # in case of authentication error
            print("Authentication Error! Return Code: " + str(rc))
            client.disconnect()
            exitFlag = True

    def on_log(self, client, userdata, level, buf):
        print("Logs: " + str(buf))

    def on_disconnect(self, pvtClient, userdata, rc):
        client.disconnect()
        print("disconnecting reason  " + str(rc))

    def return_int(self):
        return self.dest_id, self.dest_mode, self.error

def main():
    client.connect(host, port, keepAlive)
    client.loop_start()
    # time.sleep(2)
    while True:
        hey = Publisher(1, 'active_start', "None")
        data_0, data_1, data_2 = hey.return_int()
        print(data_0, data_1, data_2)
        time.sleep(1)


client.loop_stop()

if __name__ == "__main__":
    main()
