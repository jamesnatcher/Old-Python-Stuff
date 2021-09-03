user_input = input('Enter an integer number or an empty line to stop entering values ')
num_list = []
maximum = int(0)
minimum = int(0)

if user_input == '':
    print('Empty input')

while user_input != '' and user_input != ' ':
    if int(user_input) > int(maximum):
        maximum = user_input
    if int(user_input) < int(minimum):
        minimum = user_input
    num_list.append(int(user_input))
    user_input = input('Enter an integer number or an empty line to stop entering values ')
else:
    if len(num_list) > 0:
        print('Normalized values')

    for i in num_list:
        result = (i - int(minimum))/(int(maximum)-int(minimum))
        print(result)
