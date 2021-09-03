import math

''' Define your function here. '''
def max_magnitude(user_val1, user_val2):
    magnitude1 = abs(user_val1)
    magnitude2 = abs(user_val2)
    max = user_val1
    if magnitude2 > magnitude1:
        max = user_val2
    
    return max

if __name__ == '__main__':
    ''' Type your code here. '''
    num1 = int(input())
    num2 = int(input())
    print(max_magnitude(num1, num2))
