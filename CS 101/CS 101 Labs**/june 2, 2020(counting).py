'''text = input('Enter some text: ')


occurences = dict()
for c in text:
    if c in occurences:
        occurences[c] += 1
    else:
        occurences[c] = 1

print()
print(occurences)


for c in occurences:
    print('\n{} occurs {} times in {}'.format(c, occurences[c], text))'''

#program that handles multiple elements in a list

# 1.    User enters elements of a list. They enter an empty line
#       when they are done entering elements.
#       For examplle the list is ['Flower', 'Sun', 'Flower', 'Beach', 'Sun']
# 2.    Program counts the number of occurences in each elements in the list
#       that becomes a dictionary: { "Flower" : 2, "Sun" : 2, "Beach" : 1 } 
# 3.    The program converts the dictionary back to a list of couples
#       (elements, occurences)
#       That becomes a list of couples: [ ('Flower', 2), ('Sun', 2), ('Beach', 1) ]
# 4.    Program outputs this list of couples
# 5.    Revert the list of couples back to the initial user list

'''user_element = input('Enter an element or an empty line if you are done: ')
user_list = []

while user_element != '':
    user_list.append(user_element)
    user_element = input('Enter an element or an empty line if you are done: ')

occurences = dict()
for element in user_list:
    if element in occurences:
        occurences[element] +=1
    else:
        occurences[element] = 1

output_list = []
for element in occurences:
    output_list.append((element, occurences[element]))

repitition_list = []
for element in output_list:
    thing, num = element
    i = 0
    while i < num:
        repitition_list.append(thing)
        i += 1

print(repitition_list)'''

