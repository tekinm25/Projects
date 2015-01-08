# Find PI to the Nth Digit
# Enter a number and have the program generate 
# PI up to that many decimal places.

from math import pi

# Doing it this way results in the last digit being rounded
def precision():
	print("How many decimal places of pi do you want to see?")
	a = str(pi)
	x = raw_input('> ')
	try:
		if int(x) > 0 and int(x) <= 11:
			b = int(x)
			y = a[:b + 2]
			# Float the string at the end, in order to be able to use the 
			# future problems generated number in
			z = float(y)
			print z
		elif int(x) <= 0 or int(x) > 11:
			print("ValueError: Provide a positive integer that is less than 11")
			precision()
	except ValueError:
		print("ValueError: Provide an integer")
		precision()
	
precision()