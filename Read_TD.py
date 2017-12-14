# -*- coding: utf-8 -*-
"""
Created on Mon Apr 17 17:11:34 2017

@author: ZY
"""

import time
import RPi.GPIO as GPIO
import Adafruit_DHT

# Initiate the RIP sensor
GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.IN) 

j=0

#while j<100#
# Print the experiment time
def ReadData (Pin_22Sensor, Pin_11Sensor, pir_pin ):
     print (time.localtime())
    
# Temperature Sensor Read Data
     #Pin_22Sensor=4#
     #Pin_11Sensor=5#
     humidity22, temperature22 = Adafruit_DHT.read_retry(22, Pin_22Sensor)
    
     if humidity22 is not None and temperature22 is not None:
         print('Temp={0:0.1f}*  Humidity={1:0.1f}%'.format(temperature22, humidity22))
     else:
         print('Failed to get reading. Try again!')
    
     time.sleep(0.5)
    
     humidity11, temperature11 = Adafruit_DHT.read_retry(11, Pin_11Sensor)
    
     if humidity11 is not None and temperature11 is not None:
         print('Temp={0:0.1f}*  Humidity={1:0.1f}%'.format(temperature11, humidity11))
     else:
         print('Failed to get reading. Try again!')
     time.sleep(0.5)
    
    # RIP Sensor to detect human Activity
     i=0
     sum_cc=0
     while i<10: 
         CC=GPIO.input(pir_pin)
         sum_cc=sum_cc+CC
         i=i+1
         time.sleep(0.5)
     if sum_cc>7:
         Room=1
         print (Room)
         print ('The room is occupied!')
     else:
         Room=0
         print (Room)
         print ('The room is empty!')

#print ('This round finish, exit!')

while j<100:
    ReadData(4,5,18)
    j=j+1
    time.sleep(60)

GPIO.cleanup()

