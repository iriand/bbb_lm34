import time
import Adafruit_BBIO.ADC as ADC

ADC.setup()


def read_temp_values_cont():
	while(1):
		f = read_sensor()

		c = (f - 32) * 5 /9

		print "%3.1fF, %3.1fC" % (f, c)
		
		time.sleep(1)
	
def read_sensor():
	ain_value = ADC.read("P9_39")

        ain_voltage = 1.8 * ain_value

	sensor_output_voltage = ain_voltage * 2 

	f = sensor_output_voltage * 100

	return f

if __name__ == '__main__':
	read_temp_values_cont()

