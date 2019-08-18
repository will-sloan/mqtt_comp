import paho.mqtt.client as mqtt
import time
from cottage_work.mqtt_pi.light_sensor import light
from cottage_work.mqtt_pi.temp_sensor import temp

actions = {
0 : light,
1 : temp,
2 : None
3 : "quit"
}

global flag
flag = True

def start_client(broker='192.168.2.45', sub_list=['other', 'info'], client_name='client-002'):
    return broker, sub_list, mqtt.Client(client_name)

broker, sub_list, client = start_client()

pub_topic = sub_list[0]
sub_topic = sub_list[1]

def on_message(client, userdata, message, pub_topic):
    sleep(1)
    message = message.payload.decode("utf-8")
    try:
        action = actions[message]
        if action is "quit":
            global flag
            flag = False
        if action:
            client.publish(pub_topic, action())
        else:
            client.publish(pub_topic, f"{message} was recived on pi")
    except Exception as err:
        print(err)
    finally:
        print(f"Messsage recieved: {message}")

def on_connect(client, userdata, flags, rc):
    sleep(1)
    print(f"{client._client_id} has connected {rc}, flags are {flags"}

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

print(f"returning info on {pub_topic})
while flag:
    time.sleep(10)

print("Closing Temp/Light Client")
sleep(1)
client.disconnect()
client.loop_stop()
