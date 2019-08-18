
from time import sleep
from grovepi import dht


def temp(sensor = 4):

	try:
		temp, humidity = dht(sensor, 0)
		return f"temp == {temp}, humidity == {humidity}"
	except Exception as err:
		return err
	finally:
		print("Finished Read")
