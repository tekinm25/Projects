from math import pi


# use strings, lists, and lengths to avoid floats (rounding)
def precision():
	# turn pi into a string in order to tell python how many characters to print
	a = str(pi)
	x = raw_input('> ')
	y = a[:int(x) + 2]
	z = float(y)
	print z
	
precision()


def precision2():
	a = raw_input('> ')
	x = int(a)
	y = "%0.%f" % (pi, x)
	print y
	
precision2()

# use 10 to the power of (input) to determine decimal place in pi, rather than
# converting input to a string
def precision3():
	a = raw_input('> ')
	x = int(a)
	y = pi * (10 ** x)
	z = int(y)
	b = z / float(10 ** x)
	print b
	
precision3()



# Final: working
# Find PI to the Nth Digit
# Enter a number and have the program generate 
# PI up to that many decimal places.

from math import pi


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


# x = int(a)
# y = pi * (10 ** x)
# z = int(y)
# b = z / float(10 ** x)
# print b
	