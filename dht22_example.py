import OPi.GPIO as GPIO
from time import sleep

import dht22
import time
import datetime

PIN22 = 16

instance = dht22.DHT22(pin=PIN22)

while True:
    result = instance.read()
    if result.is_valid():
        print("Last valid input: " + str(datetime.datetime.now()))
        print("Temperature: %.2f C" % result.temperature)
        print("Humidity: %.2f %%" % result.humidity)

    time.sleep(1)
