''' Define your function here '''
def is_list_even(my_list):
    for i in my_list:
        if i % 2 != 0:
            return False
    return True

def is_list_odd(my_list):
    for i in my_list:
        if i % 2 == 0:
            return False
    return True

if __name__ == '__main__':
   ''' Type your code here. '''
   num_num = int(input())
   num_list = []

   for i in range(num_num):
       num = int(input())
       num_list.append(num)
    

   if is_list_even(num_list):
       print('all even')
   elif is_list_odd(num_list):
       print('all odd')
   else:
       print('not even or odd')


   
