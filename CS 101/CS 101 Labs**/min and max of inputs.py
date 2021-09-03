curr_power = 2
user_num = input()
maximum = user_num
minimum = user_num

while user_num == user_num:
    if user_num >= maximum:
        maximum = user_num
    if user_num <= minimum:
        minimum = user_num
    user_num = input()
    if user_num == 'done' or user_num == 'Done':
        break
    
print('The smallest number is {} and the biggest number is {}.'.format(minimum, maximum))
