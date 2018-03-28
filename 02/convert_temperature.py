#!/usr/bin/python3

def convert_to_fahrenheit(val):
	return float(val)*1.8 + 32.0

def convert_to_celsius(val):
	return ((float(val)) - 32)/1.8


if __name__=="__main__":
	input_message = 'Choose converter:\n 1 - Celsius to Faranheit\n 2 - Faranheit to Celsius\n'

	command=input(input_message)

	if command=='1':
		val=input('Temperature in Celsius:')
		print("{} Celsius equals {} Fahrenheit.".format(val,convert_to_fahrenheit(val)))

	


	if command=='2':
		val=input('Temperature in Fahrenheit:')
		print("{} Fahrenheit equals {} Celsius.".format(val,convert_to_celsius(val)))



		
