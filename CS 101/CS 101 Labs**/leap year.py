input_year = int(input())

''' Type your code here. '''

divisible_by_hundred = ((input_year % 100) == 0) 
divisible_by_4 = ((input_year % 4) == 0) 
divisible_by_fourhundred = ((input_year % 400) == 0) 

is_leap_year = (divisible_by_4 and (not divisible_by_hundred)) or divisible_by_fourhundred

if is_leap_year:
    print(input_year, '- leap year')
else:
    print(input_year, '- not a leap year')

'''def is_leap_year(input_year):
    divisible_by_onehundred = input_year % 100
    fraction = input_year % 4
    
    if divisible_by_onehundred == 0:
        if input_year % 400 == 0:
            print(input_year, 'is a leap year.')
        else:
            print(input_year, 'is not a leap year.')
    elif divisible_by_onehundred != 0:
        if fraction == 0:
            print(input_year, 'is a leap year.')
        if fraction > 0:
            print(input_year, 'is not a leap year.')
    return

if __name__ == '__main__':
    
    year = int(input())
    is_leap_year(year)'''

'''is_leap_year = False
   
input_year = int(input())

divisible_by_onehundred = input_year % 100
fraction = input_year % 4

if divisible_by_onehundred == 0:
    if input_year % 400 == 0:
        print(input_year, '- leap year')
    else:
        print(input_year, '- not a leap year')
elif divisible_by_onehundred != 0:
    if fraction == 0:
        print(input_year, '- leap year')
    if fraction > 0:
        print(input_year, '- not a leap year')'''
