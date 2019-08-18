import time

import paho.mqtt.client as paho
#broker="broker.hivemq.com"
try:
	broker = "192.168.2.45"

	sub_list = ["topic1", "topic2"]
	global flag 
	flag = True
	#define callback
	def on_message(client, userdata, message):
		try:
			#print(type(client))
			print(f"client is  {client._client_id}")
		except Exception as err:
			print(err)
		time.sleep(1)
		print("HERE")
		
		message = str(message.payload.decode("utf-8"))
		print(message=='bye', message, type(message))
		if message is 'bye' or message == '9':
			print("Made it in")
			global flag
			flag = False
		#print("Made it below 9 or bye")
		try:
			if  int(message) % 2 == 0:
				#print(f"trying to publish {message}")
				client.publish(sub_list[1], f"{message} message recived on pi")
		except:
			print("Message not int")
		print("received message =",message)

	client= paho.Client("client-002")
	 #create client object client1.on_publish = on_publish #assign function to callback client1.connect(broker,port)
	#establish connection client1.publish("house/bulb1","on")
	######Bind function to callback
	client.on_message=on_message
	#####
	print("connecting to broker ",broker)
	client.connect(broker)#connect
	client.loop_start() #start loop to process received messages
	print("subscribing ")
	client.subscribe(sub_list[0])#subscribe
	time.sleep(2)
	count = 0
	print("publishing")
	while flag:
		client.publish(sub_list[1],f"this is the pi at {count}")#publish
		#print(f"flag is {flag}")
		count +=1
		time.sleep(1)
	print("turning off mqtt")
	time.sleep(1)
	#client.disconnect() #disconnect
finally:
	client.disconnect()
	print("closing")
	client.loop_stop() #stop loop

