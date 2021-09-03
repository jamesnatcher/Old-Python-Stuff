numlist = list(input().split())
numlist = [int(i) for i in numlist]
numbounds = list(input().split())
numbounds = [int(i) for i in numbounds]

for num in numlist:
    if num >= numbounds[0] and num <= numbounds[1]:
        print(num, end=' ')
