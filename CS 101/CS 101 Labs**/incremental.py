num1 = int(input('First integer (has to be less than or equal to the second integer): '))
num2 = int(input('Second integer: '))
increments = int(input('Increment wanted: '))
result = 0
difference = num2 - num1

if increments > difference:
    print('Increments cannot be bigger than the difference of the two integers')
while num1 <= num2:
    print('Initial integer and subsequent increments')
    for i in range(num1 + increments, num2 + 1, increments):
        print(i, end=' ')
    break
else:
    print('Second integer can\'t be less than the first.')
print()
