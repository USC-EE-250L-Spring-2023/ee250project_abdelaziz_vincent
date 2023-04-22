import paho.mqtt.client as mqtt
import time
import grovepi
import math
from datetime import datetime
import socket

#https://github.com/DexterInd/GrovePi/blob/master/Projects/Home_Weather_Display/Home_Weather_Display.py
from grovepi import *
from grove_rgb_lcd import *

# Connections
led = 3                 # port D3
ultrasonic_ranger = 4   # port D4
dht_sensor_port = 2     # port D2
dht_sensor_type = 0     # use 0 for the blue-colored sensor and 1 for the white-colored sensor

# Connect to server
def on_connect(client, userdata, flags, rc):
    print("Connected to server (i.e., broker) with result code "+str(rc))


setRGB(0,0,255) #BLUE LCD starting color
pinMode(led,"OUTPUT")

if __name__ == '__main__':
    #ip_address = "192.168.64.1" #Computer Terminal
    ip_address = "192.168.1.26" #RPI

    #create a client object
    client = mqtt.Client()
    #attach the on_connect() callback function defined above to the mqtt client
    client.on_connect = on_connect

    client.connect(host="eclipse.usc.edu", port=11000, keepalive=60)

    client.loop_start()
    time.sleep(1)

    while True:

        # 5 seconds for the pre-program
        # blink LED 5 times to indicate system is booting/restarting
        for i in range (0,5):
            #blink LED
            digitalWrite(led,1) #ON
            time.sleep(0.5)
            digitalWrite(led,0) #OFF
            time.sleep(0.5)
            setText("System starting\n" + "(Please wait...)")

        
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
            
            if distance > threshold:
                setRGB(255,0,0) #RED
                setText("Person NOT in\nrange! *WALK IN*")
            else:
                setRGB(0,255,0) #GREEN
                setText("Temp:" + t + "C\n" + "Humidity :" + h + "%")

                #publish temperature
                client.publish("fuv/temp", f"{t}")
                print("Publishing temperature")
                #publish humidity
                client.publish("fuv/humid", f"{h}")
                print("Publishing humidity")

            time.sleep(1)