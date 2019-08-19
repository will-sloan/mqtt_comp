from time import sleep
from grovepi import pinMode, analogRead

def light(sensor = 0):
	pinMode(sensor, "INPUT")

	try:
		return analogRead(sensor)
	except Exception as err:
		return err
	finally:
		print("Finished Read")
