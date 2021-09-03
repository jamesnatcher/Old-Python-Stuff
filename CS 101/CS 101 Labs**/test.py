upper = 0
lower = 0

text = input()

for c in text:
    if c.isupper():
        upper +=1
    elif c.islower():
        lower += 1

print(upper, lower)
