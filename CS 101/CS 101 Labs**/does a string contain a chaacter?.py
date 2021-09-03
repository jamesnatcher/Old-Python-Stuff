def checker(char, usr_str):
    old_list = usr_str.split()
    new_list = []
    for word in old_list:
        if char in word:
            new_list.append(word)
    print('List of words with character:')
    for word in new_list:
        print(word)


character = input('Enter a character: ')
string = input('Enter the string of words to see if the character is in it: ')
checker(character, string)
