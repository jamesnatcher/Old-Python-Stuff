''' Define your function here '''
def get_user_values():
    num_values = int(input())
    num_list = []
    for i in range(num_values):
        num_actual = int(input())
        num_list.append(num_actual)
    num_thresh = int(input())
    return num_list, num_thresh
def output_ints_less_than_or_equal_to_threshold(user_values, upper_threshold):
    for (index, value) in enumerate(user_values):
        if value <= upper_threshold:
            print(value)

if __name__ == '__main__':
    user_values, upper_threshold = get_user_values()
    output_ints_less_than_or_equal_to_threshold(user_values, upper_threshold)

'''num_entry_num = int(input('How much numbers do you want to check under a certain threshold? '))
numlist = []
numlist_output = []
l = 0

for i in range(num_entry_num):
    l += 1
    num_actual = int(input('Number {}: '.format(l)))
    numlist.append(num_actual)
    
num_thresh = int(input('What is the threshold? '))
print(num_thresh)

for (index, value) in enumerate(numlist):
    if value <= num_thresh:
        print('Numbers in the threshold:', value, end=' ')'''
    
