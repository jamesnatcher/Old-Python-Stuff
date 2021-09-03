
int_nums = [int(i) for i in input().split(' ')]

positive_nums = [i for i in int_nums if i > 0]

positive_nums.sort()

for i in positive_nums:
    print(i, end=' ')
print()
