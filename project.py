import twitter
import time
import grovepi
import math

#https://github.com/DexterInd/GrovePi/blob/master/Projects/Home_Weather_Display/Home_Weather_Display.py
#from grovepi import *
from grove_rgb_lcd import *
#from time import sleep
#from math import isnan

# Connections
temperature_sensor = 2  # port D2
led = 3                 # port D3
ultrasonic_ranger = 4   # port D4
dht_sensor_port = 7     # port 7
dht_sensor_type = 0     # use 0 for the blue-colored sensor and 1 for the white-colored sensor

# set green as backlight color
# we need to do it just once
# setting the backlight color once reduces the amount of data transfer over the I2C line
setRGB(255,0,0) #RED LCD

pinMode(led,"OUTPUT")


while True:

    # 5 seconds for the pre-program
    # blink LED 5 times to indicate system is booting/restarting
    for i in range (0,5):
        #blink LED
        digitalWrite(led,1) #ON
        time.sleep(0.5)
        digitalWrite(led,0) #OFF
        time.sleep(0.5)
        setText("System starting\n" + "(Please wait ...)")

    
    # 10 seconds for the main program to run
    for i in range (0,100):
        # range sensor
        distance = ultrasonicRead(ultrasonic_ranger)
        print(distance,'cm')
        threshold = 69 #CHANGE THIS LATER

        # temp&humd sensor
        [ temp,hum ] = dht(dht_sensor_port,dht_sensor_type)
        print("temp =", temp, "C\thumidity =", hum,"%")
        t = str(temp)
        h = str(hum)
        # instead of inserting a bunch of whitespace, we can just insert a \n
        # we're ensuring that if we get some strange strings on one line, the 2nd one won't be affected
        # LCD
        setText_norefresh("Temp:" + t + "C\n" + "Humidity :" + h + "%")
        if distance > threshold:
            setRGB(0,255,0) #GREEN
        else:
            setRGB(255,0,0) #RED

        time.sleep(0.1)
