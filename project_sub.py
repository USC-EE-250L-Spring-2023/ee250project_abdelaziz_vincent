import paho.mqtt.client as mqtt

def on_connect(client, userdata, flags, rc):
    
    print("Connected to server (i.e., broker) with result code "+str(rc))

    client.subscribe("fuv/temp")
    client.subscribe("fuv/humid")

    #Add the custom callbacks by indicating the topic and the name of the callback handle
    client.message_callback_add("fuv/temp", on_message_from_temp)
    client.message_callback_add("fuv/humid", on_message_from_humid)


def on_message(client, userdata, msg):
    print("Default callback - topic: " + msg.topic + "   msg: " + str(msg.payload, "utf-8"))

#Custom message callback for temp
def on_message_from_temp(client, userdata, message):
   print("VHE 205 Temperature: "+ message.payload.decode() + "C")

#Date message callback for humid
def on_message_from_humid(client, userdata, message):
   print("VHE 205 Humidity: " + message.payload.decode() + "%\n")


if __name__ == '__main__':
    #create a client object
    client = mqtt.Client()
    #attach a default callback which we defined above for incoming mqtt messages
    client.on_message = on_message
    #attach the on_connect() callback function defined above to the mqtt client
    client.on_connect = on_connect

    #USC Server: "eclipse.usc.edu" OR "68.181.32.115"
    client.connect(host="192.168.2.31", port=1883, keepalive=60) 
    client.loop_forever()
