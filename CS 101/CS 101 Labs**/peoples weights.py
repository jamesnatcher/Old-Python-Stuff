weight_list = []

weight1 = float(input('Enter weight 1:\n'))
weight_list.append(weight1)
weight2 = float(input('Enter weight 2:\n'))
weight_list.append(weight2)
weight3 = float(input('Enter weight 3:\n'))
weight_list.append(weight3)
weight4 = float(input('Enter weight 4:\n'))
weight_list.append(weight4)

print('Weights:', weight_list)
print()

weightsum = 0
for weight in weight_list:
    weightsum += weight

print('Average weight: {:.2f}'.format(weightsum/len(weight_list)))
print('Max weight: {:.2f}'.format(max(weight_list)))
print()

list_location = int(input('Enter a list location (1 - 4):\n'))
print('Weight in pounds: {:.2f}'.format(weight_list[list_location - 1]))
print('Weight in kilograms: {:.2f}'.format((weight_list[list_location - 1])/2.2))
print()

weight_list.sort()
print('Sorted list:', weight_list)
