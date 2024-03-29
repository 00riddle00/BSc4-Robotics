"""
MicroPython: ESP8266 with DHT11 Temperature and Humidity Sensor
"""

from time import sleep

import dht
import machine

sensor = dht.DHT11(machine.Pin(14))

while True:
    try:
        sleep(2)
        sensor.measure()
        temp = sensor.temperature()
        hum = sensor.humidity()
        temp_f = temp * (9/5) + 32.0
        print('Temperature: %3.1f C' %temp)
        print('Temperature: %3.1f F' %temp_f)
        print('Humidity: %3.1f %%' %hum)
    except OSError as e:
        print('Failed to read sensor.')
