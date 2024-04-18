## Serial code to connect to the arduino
python -m venv client_env
.\client_env\Scripts\activate

pip install pyserial  
pip install paho-mqtt 

### Command
client_env\Scripts\activate && cd arduino_code && python mqtt_led_serial.py