''' Define your function here. '''
def integer_to_reverse_binary(integer_value):
    string = ''
    while integer_value > 0:
        remainder = integer_value % 2
        string = string + (str(remainder))
        integer_value = integer_value // 2
    return string

def reverse_string(input_string):
    return input_string[::-1]
    
if __name__ == '__main__':
    ''' Type your code here. Your code must call the function. '''
    num = int(input())
    print(reverse_string(integer_to_reverse_binary(num)))

'''num = int(input())
line = []
while num > 0:
    remainder = num % 2
    line.append(int(remainder))
    num = num //2 
line.reverse()
for i in line:
    print(i, end='')
print()'''
