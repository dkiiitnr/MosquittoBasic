/*
  Basic ESP8266 MQTT example
  This sketch demonstrates the capabilities of the pubsub library in combination
  with the ESP8266 board/library.
  It connects to an MQTT server then:
  - publishes "hello world" to the topic "outTopic" every two seconds
  - subscribes to the topic "inTopic", printing out any messages
    it receives. NB - it assumes the received payloads are strings not binary
  - If the first character of the topic "inTopic" is an 1, switch ON the ESP Led,
    else switch it off
  It will reconnect to the server if the connection is lost using a blocking
  reconnect function. See the 'mqtt_reconnect_nonblocking' example for how to
  achieve the same result without blocking the main loop.
  To install the ESP8266 board, (using Arduino 1.6.4+):
  - Add the following 3rd party board manager under "File -> Preferences -> Additional Boards Manager URLs":
       http://arduino.esp8266.com/stable/package_esp8266com_index.json
  - Open the "Tools -> Board -> Board Manager" and click install for the ESP8266"
  - Select your ESP8266 in "Tools -> Board"
*/

#include <ESP8266WiFi.h>
#include <PubSubClient.h>

// Update these with values suitable for your network.

const char* ssid = "Suyash";
const char* password = "Suyash@1234";
const char* mqtt_server = "192.168.43.1";
char new_payload[30];

WiFiClient espClient;
PubSubClient client(espClient);

unsigned long lastMsg = 0;
#define MSG_BUFFER_SIZE	(50)

const char* pub_frame_topic = "unbox/frame_to_aggregator";
const char* sub_frame_topic = "unbox/frame_to_dest";


long loopcount = 0;
bool isDone = false;



uint8_t dest_ids[] = {1, 2, 3, 4};
uint8_t dest_modes[] = {1, 2, 3, 4, 5};
uint8_t parcel_statuses[] = {1, 2, 3};

struct dest_frame
{
  uint8_t dest_id;
  uint32_t pincode;
  uint8_t parcel_status;
  uint8_t modes;
  uint8_t bag_presence;
  uint8_t bag_position;
};

struct dest_frame my_frame = {0};

char msg[MSG_BUFFER_SIZE];
int value = 0;

void setup_wifi() {

  delay(10);
  // We start by connecting to a WiFi network
  Serial.println();
  Serial.print("Connecting to ");
  Serial.println(ssid);

  WiFi.mode(WIFI_STA);
  WiFi.begin(ssid, password);

  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }

  randomSeed(micros());

  Serial.println("");
  Serial.println("WiFi connected");
  Serial.println("IP address: ");
  Serial.println(WiFi.localIP());
}

void callback(char* topic, byte* payload, unsigned int length) {
  Serial.print("Message arrived [");
  Serial.print(topic);
  Serial.print("] ");
  for (int i = 0; i < length; i++) {
    Serial.print((char)payload[i]);
  }
  Serial.println();
  if ((char)payload[0] == '1') {
    digitalWrite(BUILTIN_LED, LOW);
  } else {
    digitalWrite(BUILTIN_LED, HIGH);
  }

}

void reconnect() {
  // Loop until we're reconnected
  while (!client.connected()) {

    String clientId = "ESP8266Client-";
    clientId += String(random(1000), DEC);

    // Attempt to connect

    if (client.connect(clientId.c_str())) {
      Serial.println("connected");
      client.subscribe("unbox/frame_to_dest");
    }
    else {
      Serial.print("failed, rc=");
      Serial.print(client.state());
      Serial.println(" try again in 5 seconds");
      // Wait 5 seconds before retrying
      delay(5000);
    }
  }
}

void creat_random_frame() {
  my_frame.dest_id = dest_ids[(random(0, 3))];
  my_frame.pincode = (random(400001, 410000));
  my_frame.parcel_status = parcel_statuses[(random(0, 2))];
  my_frame.modes = dest_modes[random(0, 4)];
  my_frame.bag_presence = (random(0, 1));
  my_frame.bag_position = (random(0, 1));
}


void setup() {
  pinMode(BUILTIN_LED, OUTPUT);     // Initialize the BUILTIN_LED pin as an output
  Serial.begin(115200);
  setup_wifi();
  client.setServer(mqtt_server, 1883);
  client.setCallback(callback);
}

void loop() {

  if (!client.connected()) {
    reconnect();
  }

  for (int i = 0; i <= 500; i++)
  { if (isDone != true){
    
      creat_random_frame();
      String payload = String(my_frame.dest_id) + String(my_frame.pincode) + String(my_frame.modes) + String(my_frame.parcel_status) + String(my_frame.bag_position) + String(my_frame.bag_presence) + String("3");
      int payload_length = payload.length();
      char new_payolad[payload_length + 1];
      strcpy(new_payload, payload.c_str());
      client.publish(pub_frame_topic, new_payload);
      Serial.print(my_frame.dest_id); Serial.print("/");
      Serial.print(my_frame.pincode); Serial.print("/");
      Serial.print(my_frame.modes); Serial.print("/");
      Serial.print(my_frame.parcel_status); Serial.print("/");
      Serial.print(my_frame.bag_position); Serial.print("/");
      Serial.print(my_frame.bag_presence);Serial.print("/");
      Serial.print(new_payload[11]);Serial.print(" ");
      Serial.println(i);
      delay(200);
  }
    if(i == 500){
      isDone = true;
    }
  }
  //  delay(2000);


  client.loop();
}
