# Find PI to the Nth Digit
# Enter a number and have the program generate 
# PI up to that many decimal places.

from math import pi

# Doing it this way allows you to generate pi to the desired
# decimal place (below 12) without having the last digit rounded
def precision():
	a = raw_input('> ')
	try:
		if int(a) > 0 and int(a) < 12:
			x = int(a)
			y = pi * (10 ** x)
			z = int(y)
			b = z / float(10 ** int(x))
			print b
			print pi
		elif int(a) <= 0 or int(a) >= 12:
			print "Error: Input must be a positive integer and less than 12"
			precision()
	except ValueError:
		print "ValueError: Input be an integer"
		precision()
	
precision()