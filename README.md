DHT22 Python library
This simple class can be used for reading temperature and humidity values from DHT22 sensor on Orange PI 3 LTS. Using library https://github.com/koguja/OrangePi.GPIO

# Usage

Example:
```python
import OPi.GPIO as GPIO

GPIO.setboard(GPIO.THREE)
GPIO.setmode(GPIO.BOARD)

import dht22
import time
import datetime
 
# initialize GPIO

PIN22 = 16
 
# read data using pin 14
instance = dht22.DHT22(pin=PIN22)
 
while True:
    result = instance.read()
    if result.is_valid():
        print("Last valid input: " + str(datetime.datetime.now()))
        print("Temperature: %.2f C" % result.temperature)
        print("Humidity: %.2f %%" % result.humidity)
 
    time.sleep(1)
```    
Please see tutorial:
http://www.piprojects.xyz/temperature-sensor-orange-pi-python-code/
