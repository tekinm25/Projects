# Find e to the Nth Digit
# Enter a number and have the program generate 
# e up to that many decimal places.

from math import e

# Doing it this way allows you to generate e to the desired
# decimal place (below 12) without having the last digit rounded
def precision():
    print("How many decimal places of e do you want to see?")
    a = str(e)
    x = raw_input('> ')
    try:
        if int(x) > 0 and int(x) <= 11:
            b = int(x)
            y = a[:b + 2]
            # Float the string at the end, in order to be able to use the 
            # future problems generated number in
            z = float(y)
            print z
            print e
        elif int(x) <= 0 or int(x) > 11:
            print("ValueError: Provide a positive integer that is less than 11")
            precision()
    except ValueError:
        print("ValueError: Provide an integer")
        precision()
    
precision()