from time import sleep
from grovepi import pinMode, analogRead

def light(sensor = 0):
	pinMode(sensor, "INPUT")

	try:
		print(analogRead(sensor))
	except Exception as err:
		print(err)
	finally:
		print("Finished Read")
