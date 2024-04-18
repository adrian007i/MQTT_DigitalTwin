import paho.mqtt.client as mqtt 
import serial
import threading   

# dependencies
# pip install pyserial  
# pip install paho-mqtt 

def on_connect(client, userdata, flags, reason_code, properties): 
    print("mqtt connected")
    client.subscribe("led_status")

def on_message(client, userdata, msg):
    changeLEDStatus(msg.payload.decode()) 


mqttc = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
mqttc.password = "password"
mqttc.username="user1"
mqttc.on_connect = on_connect
mqttc.on_message = on_message

mqttc.connect("127.0.0.1", 1883, 60)
mqttc.loop_start()
 
ser = serial.Serial('COM3', 115200)  

if ser.isOpen():
    print('The Arduino is Connected')


def changeLEDStatus(status): 
    status = int(status)
    buffer = [0xff, 0x55, 0x5, 0x0, 0x2, 0x22, 0x9, status]
    ser.write(ser.write(serial.to_bytes(buffer)))

try:
    while True:
        try:
            data = ser.read(1)  # Read a single byte
            if data:
            # Interpret the received data
                button_state = int.from_bytes(data, byteorder='big') 
                if button_state == 1 or button_state == 0: 
                    mqttc.publish("led_status", button_state)  
        except Exception as err:
            print(err)
except KeyboardInterrupt:
    print("\nLoop interrupted by user.") 


# command to run
# cd "C:\Users\Adrian John\Desktop\Work\Digital Twin\twinmaker_websocket\arduino" && arduino\Scripts\activate && cd led && python mqtt_led_serial.py


 
 

 
