import paho.mqtt.client as mqtt
import time
try:
    broker="192.168.2.45"
    sub_list = ["info", "other"]
    #define callback
    def on_message(client, userdata, message):
        time.sleep(1)
        print("received message =",str(message.payload.decode("utf-8")))

    client= mqtt.Client("client-001") #create client object client1.on_publish = on_publish #assign function to callback client1.connect(broker,port) #establish connection client1.publish("house/bulb1","on")
    ######Bind function to callback

    client.on_message=on_message
    #####
    print("connecting to broker ",broker)
    client.connect(broker)#connect
    client.loop_start() #start loop to process received messages
    print("subscribing ")
    client.subscribe(sub_list[1])#subscribe
    time.sleep(2)
    print("publishing ")
    for i in range(5,10):
        if i == 9:
            client.publish(sub_list[0], "quit")
        if i%2==0:
            client.publish(sub_list[0],"temp")#publish
        else:
            client.publish(sub_list[0], "light")
        time.sleep(5)
    time.sleep(10)

finally:
    client.disconnect() #disconnect
    print("ending")
    client.loop_stop() #stop loop
