nums = input().split()
nums = [int(i) for i in nums]

def positive(nums):
    positive_nums = []

    for num in nums:
        if num >= 0:
            positive_nums.append(num)
    return positive_nums
    
def sort(numlist):
    numlist.sort()
    return numlist

for i in (sort(positive(nums))):
    print(i, end=' ')
