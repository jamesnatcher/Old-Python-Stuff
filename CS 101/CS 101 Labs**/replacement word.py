rawreplace = list(input().split('   '))
replace_dict = dict(pair.split() for pair in rawreplace)

sentence = input().split()
new_sentence = []

for word in sentence:
    if word in replace_dict:
        word = replace_dict[word]
        new_sentence.append(word)
    else:
        new_sentence.append(word)

print(' '.join(new_sentence))
