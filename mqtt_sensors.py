import paho.mqtt.client as mqtt
from time import sleep
from light_senor import light
from temp_sensor import temp

actions = {
"light" : light,
"temp" : temp,
"quit" : "quit"
}

global flag
flag = True

def start_client(broker='192.168.2.45', sub_list=['other', 'info'], client_name='client-002'):
    return broker, sub_list, mqtt.Client(client_name)

broker, sub_list, client = start_client()

pub_topic = sub_list[0]
sub_topic = sub_list[1]

def on_message(client, userdata, message):
    print("recived message")
    sleep(1)
    message = str(message.payload.decode("utf-8").strip())
    #q = 'quit'
    #try:
    #    print(type(message), type(q), id(message), id(q))
    #except Exception as err:
    #    print(err)
    try:
        #print(message == 'quit', message is "light", message is "temp")
        if message == "quit":
            print("setting flag to false")
            global flag
            flag = False
        elif message == "light":
            print("getting light")
            client.publish(pub_topic, light())
        elif message == "temp":
            print("getting temp")
            client.publish(pub_topic, temp())
        else:
            client.publish(pub_topic, f"{message} was recived on pi")
    except Exception as err:
        print(err)
    finally:
        print(f"Messsage recieved: {message}")

def on_connect(client, userdata, flags, rc):
    sleep(1)
    print(f"{client._client_id} has connected {rc}, flags are {flags}")

def on_disconnect(client, userdata, rc):
    sleep(1)
    print(f"{client._client_id} has diconnected {rc}")

client.on_message = on_message
client.on_connect = on_connect
client.on_disconnect = on_disconnect

client.connect(broker)
client.loop_start()

sleep(1)

print(f"listening on {sub_topic}")
client.subscribe(sub_topic)

print(f"returning info on {pub_topic}")
while flag:
    client.publish(pub_topic, "Here\n")
    sleep(1)

print("Closing Temp/Light Client")
sleep(1)
client.disconnect()
client.loop_stop()
