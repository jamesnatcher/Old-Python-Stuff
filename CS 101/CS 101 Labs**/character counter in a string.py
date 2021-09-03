def count_characters(character, usr_str):
    count = 0
    for i in usr_str:
        if i == character:
            count += 1
    return count 


usr_str = input('Enter the desired character, spacebar, then the string to count from (case sensitive): ')
usr_char = usr_str[0]
tru_str = usr_str[1:]


print('Number of occurence: ', count_characters(usr_char, tru_str))
