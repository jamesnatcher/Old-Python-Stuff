nums = list(input().split())

def average(nums):
    sum = 0
    for i in nums:
        sum += int(i)
    average = sum / len(nums)
    return average

def biggest(nums):
    big = int(0)
    for i in nums:
        if int(i) > int(big):
            big = i
    return big

print('{:.0f} {}'.format(average(nums), biggest(nums)))
