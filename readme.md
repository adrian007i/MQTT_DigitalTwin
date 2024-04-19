# Digital Twin Platform
This was developed because the existing AWS digital twin architectured had a couple issues.

## Issues with AWS Digital Twin
- Platform was slow, resulting in 4 second delays
- Did not support bi-directional interaction within the digital twin

##  Tech
- Babylon.js - (HTML, CSS, JS)
- MQTT (eclipse-mosquitto) with docker
- arduino uno with python serial communication

## Architecture 
![Diagram](Diagram.png)

## Deployment for Windows (Assuming you already have docker)
1)  ### Backend
    This will setup and configure influxDB and the MQTT Broker.
    ```
    cd backend
    docker-compose up 
    
    # For more info on deploying MQTT and Influxdb checkout:
    # https://hub.docker.com/_/influxdb
    # https://github.com/sukesh-ak/setup-mosquitto-with-docker
    ```
 
2)  ### Digital Twin UI
    This is a pure HTML CSS JS application with the use of a couple javascript library.  No resources is needed to run this.  Simply open digital_twin_ui/digital_twin.html in the browser.


3) ### Install Client Dependencies 

    ``` 
    pip install pyserial  
    pip install paho-mqtt
    ``` 

4) ### Arduino Setup
    You need to do 2 things to setup the arduino:
    1. Use arduino IDE to import the code unto the arduino,  The code to import is called ```/arduino_code/main_arduino.ino```
    2. You need to run the python serial code.  This will listen for changes on the MQTT broker and it will also be used to publish changes to MQTT broker.  When changes are made on the MQTT broker, the python serial code will command the arduino.  
    
        ```To run this, you must run the python arduino_code/mqtt_led_serial.py```

5) ### Run InfluxDB Python Script
    This script will listen for changes via the MQTT broker. Once a change is detected, it will store it in InfluxDB.  No server is needed here.  This is just a client.
    
    ```To run this, you must run the python backend/influx_db_script.py```
 