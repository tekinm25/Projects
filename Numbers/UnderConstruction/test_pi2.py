def precision():    
    s = raw_input("How many digits of pi do you want to see? ")
    if int(s) >= 10000:
        print "Enter a number smaller than 10000."
    elif int(s) > 0:
        print int(s) 
    else:
        print "Enter a nonnegative integer."
			
precision()