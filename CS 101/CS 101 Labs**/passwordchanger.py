word = input()
password = ''
endadd = 'q*s'
replaced = {
    'i': '!',
    'a': '@',
    'm': 'M',
    'B': '8',
    'o': '.'}

for character in word:
    if character in replaced:
        character = replaced[character]
    else:
        character = character
    password += character 
     
print('{}{}'.format(password, endadd))
