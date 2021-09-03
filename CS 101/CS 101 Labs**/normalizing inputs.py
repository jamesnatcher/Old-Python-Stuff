num_num = int(input())
minimum = int()
list1 = []

for i in range(num_num):
    num = int(input())
    list1.append(num)

for (index, value) in enumerate(list1):
    result = value - min(list1)
    print(result)
