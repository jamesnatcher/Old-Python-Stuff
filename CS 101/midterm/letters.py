string = input('Please enter a line of text: ')

upper_count = 0
lower_count = 0
punctuation_count =0
unknown = 0
space_count = 0

for c in string:
    if ((ord('A') <= ord((c)) and (ord(c)) <= ord('Z'))):
        upper_count += 1
    elif ((ord('a') <= ord((c)) and (ord(c)) <= ord('z'))):
        lower_count += 1
    elif c in '.\’,;:!?&/':
        punctuation_count +=1
    elif c == ' ':
        space_count +=1 
    else: 
        unknown += 1

print('The text "{}\" contains'.format(string))

print('* {} upper-case characters,'.format(upper_count))
print('* {} lower-case characters,'.format(lower_count))
print('* {} punctuation signs and'.format(punctuation_count))
print('* {} foreign writing system characters.'.format(unknown))
