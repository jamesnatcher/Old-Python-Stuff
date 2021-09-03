#################################################################
#
#  Paul James NATCHER
#
#################################################################

# Points possible: 12
def centimeters_to_us_units(cm):
    amount = cm
    miles = int((amount)) // int(160934.4)
    yards = int((amount) % 160934.4 ) // int(91.44)
    feet = int((amount) % 160934.4 % 91.44) // int(30.48)
    inches = ((((amount % 160934.4) % 91.44) % 30.48)) / float(2.54)
    return (miles, yards, feet, inches)


# Points possible: 5
def us_units_to_centimeters(length):
    a, b ,c, d = length
    inch = float(d) * 2.54
    foot = float(c) * 30.38
    yard = float(b) * 91.44
    miles = float(a) * 160934.4
    total = inch + foot + yard + miles
    
    return total


# Points possible: 10
def mpg_to_liters_per_hundred_kilometers(mpg):
    if mpg == 0:
        return 0
    else:
        lpk = (100 * 3.785411784) / (mpg * 1.609344 )
    return lpk


