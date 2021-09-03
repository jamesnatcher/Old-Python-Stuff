text = input('Enter some text')


occurences = dict()
for c in text:
    if c in occurences:
        occurences[c] += 1
    else:
        occurences[c] = 1

print(occurences)
