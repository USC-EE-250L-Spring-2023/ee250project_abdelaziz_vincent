# ee250project_abdelaziz_vincent

Team Members:
1 - Vincent Fu
2 - Abdelaziz Abdelrhman

Link to video demo:
https://drive.google.com/drive/folders/1zAg5flioCcb34FQDe35N5wvLlE4IKUrf?usp=sharing

Instructions on how to compile/execute our code (given that the circuitry and hardware is all set up and all external libraries are downloaded):
1) Make sure there is an Rpi set up as a broker before starting anything.
2) On your PC, open up your terminal and cd into the directory that contains project_sub.py.
3) Open up a new terminal window and ssh into a different Rpi (that isn't the broker).
4) Open up a new terminal window and cd into the directory that contains project_pub.py.
5) Send the project_pub.py file to the Rpi you ssh-ed into (using scp, copy-paste, etc).
6) Run project_sub.py in its terminal.
7) Run project_pub.py on the Rpi. 
9) Watch our project work!

External Libraries used in our code:
1) import paho.mqtt.client as mqtt
2) import time
3) import grovepi
4) import math
5) from datetime import datetime
6) import socket

Used the following link to help us figure out the rest of the needed libraries:
#https://github.com/DexterInd/GrovePi/blob/master/Projects/Home_Weather_Display/Home_Weather_Display.py

7) from grovepi import *
8) from grove_rgb_lcd import *
