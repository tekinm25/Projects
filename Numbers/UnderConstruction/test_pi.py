def precision():    
	s = raw_input("How many digits of pi do you want to see? ")
        try:
            digits = int(s)
            if digits >= 10000:
                print "Enter a number smaller than 10000."
            elif digits > 0:
                print digits 
            else:
                print "Enter a nonnegative integer."
        except ValueError:
            print "Enter a nonnegative integer."
			
precision()