# Find PI to the Nth Digit
# Enter a number and have the program generate 
# PI up to that many decimal places.

from math import pi


def precision():
	# Use strings, lists, and lengths to avoid rounding
	a = str(pi)
	x = raw_input('> ')
	# Float the string in order to be able to use the generated number in
	# future problems
	# if the given input is anything other than a positive integer less than 11,
	# print "ValueError: Provide a positive integer less than 11"
	try:
		# if the input is a positive integer less than 11 then use it to
		# determine the decimal place in pi
		if int(x) > 0 and int(x) <= 11:
			b = int(x)
			y = a[:b + 2]
			z = float(y)
			print z
		# if the input is negative or greater than 1000 print value error and
		# try again
		elif int(x) <= 0 or int(x) > 11:
			print "ValueError: Provide a positive integer that is less than 11"
			precision()
	# if the input is not an integer
	except ValueError:
		print("ValueError: Provide an integer")
		precision()
	
precision()