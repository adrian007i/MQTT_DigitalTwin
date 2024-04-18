## Serial code to connect to the arduino
- python -m venv client_env
- .\client_env\Scripts\activate
- pip install pyserial  
- pip install paho-mqtt 

### Command
client_env\Scripts\activate && cd arduino_code && python mqtt_led_serial.py

## Steps to setup the MQTT broker
- for docker setup, follow this guide:  https://github.com/sukesh-ak/setup-mosquitto-with-docker 