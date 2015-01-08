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