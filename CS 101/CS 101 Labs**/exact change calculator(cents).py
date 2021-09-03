dollar = 100
quarter = 25
dime = 10
nickel = 5
penny = 1
remainder = 0
terminate = int()

''' Define your function here '''
def exact_change(number):
    dollar_out = number // 100
    quarter_out = (number % 100) // 25
    dime_out = (number % 100 % 25) // 10
    nickel_out = (number % 100 % 25 % 10) // 5
    penny_out = (number % 100 % 25 % 10 % 5) // 1      
    return dollar_out, quarter_out, dime_out, nickel_out, penny_out
    
if __name__ == '__main__': 
    input_val = int(input())    
    dollar_out, quarter_out, dime_out, nickel_out, penny_out = exact_change(input_val)

    ''' Type your code here. '''
    if input_val <= 0:
            print('no change')
    if dollar_out > 1:
        print(dollar_out, 'dollars')
    if dollar_out == 1:
        print(dollar_out, 'dollar')
    if quarter_out > 1:
        print(quarter_out, 'quarters')
    if quarter_out == 1:
        print(quarter_out, 'quarter')
    if dime_out > 1:
        print(dime_out, 'dimes')
    if dime_out == 1:
        print(dime_out, 'dime')
    if nickel_out  > 1:
        print(nickel_out, 'nickels')
    if nickel_out  == 1:
        print(nickel_out, 'nickel')
    if penny_out > 1:
        print(penny_out, 'pennies')
    if penny_out == 1:
        print(penny_out, 'penny')


'''print('Enter dollar value:')
number = float(input())


number = number * 100
dollar_out = number // dollar
quarter_out = (number % 100) // quarter
dime_out = (number % 100 % 25) // dime
nickel_out = (number % 100 % 25 % 10) // nickel
penny_out = (number % 100 % 25 % 10 % 5) // penny


while terminate > 1:
    if number <= 0:
        print('No change')
    if dollar_out > 1:
        print(dollar_out, 'Dollars')
    if dollar_out == 1:
        print(dollar_out, 'Dollar')
    if quarter_out > 1:
        print(quarter_out, 'Quarters')
    if quarter_out == 1:
        print(quarter_out, 'Quarter')
    if dime_out > 1:
        print(dime_out, 'Dimes')
    if dime_out == 1:
        print(dime_out, 'Dime')
    if nickel_out  > 1:
        print(nickel_out, 'Nickels')
    if nickel_out  == 1:
        print(nickel_out, 'Nickel')
    if penny_out > 1:
        print(penny_out, 'Pennies')
    if penny_out == 1:
        print(penny_out, 'Penny')
    number = float(input())
    terminate = input()'''
    

