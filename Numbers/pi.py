# Find PI to the Nth Digit


from math import pi


def precision():
	# Enter a number and have the program generate 
	# PI up to that many decimal places.
	# Use strings, lists, and lengths to avoid rounding
	a = str(pi)
	x = int(raw_input('> '))
	y = a[:x + 1]
	# Float the string in order to be able to use the generated number in
	# future problems
	z = float(y)
	print z
	
	# Keep a limit to how far the program will go.
	
precision()