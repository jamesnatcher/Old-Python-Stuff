# Type all other functions here

def print_menu(usr_str):
    menu_op = '\nMENU\nc - Number of non-whitespace characters\nw - Number of words\nf - Fix capitalization\nr - Replace punctuation\ns - Shorten spaces\nq - Quit\n\nChoose an option:'
    # Complete print_menu() function
  
    while True:
        print(menu_op)
        user_choice = input()
        if user_choice == 'q':
            break
        elif user_choice == 'c':
            print('\nNumber of non-whitespace characters:', get_num_of_non_WS_characters(usr_str))
        elif user_choice == 'w':
            print('\nNumber of words:', get_num_of_words(usr_str))
        elif user_choice == 'f':
            d, e = fix_capitalization(usr_str)
            print('Number of letters capitalized: {}\nEdited text: {}'.format(e, d))
        elif user_choice == 'r':
            #FIXME
            print('Punctuation replaced\nexclamation\_count: {}\nsemicolon\_count: {}\nEdited text: {}'.format(replace_punctuation.exclamation_count, replace_punctuation.semicolon_count, replace_punctuation(usr_str)))
        elif user_choice == 's':
            print('Edited text:', shorten_space(usr_str))
    return menu_op, usr_str
def get_num_of_non_WS_characters(usr_str):
    spaces = 0
    for character in usr_str:
        if character == ' ' or character == '\t':
            spaces += 1
    return len(usr_str) - spaces
def get_num_of_words(usr_str):
    words = usr_str.split()
    count = 0
    for word in words:
        if word in words:
            count += 1
        else:
            count = 1 
    return count

def fix_capitalization(usr_str):
    count = 0
    beginning = True
    new_str = ''
    for i in usr_str:
        if beginning and i.isalpha():
            if i.islower():
                i = i.upper()
                count += 1
                new_str += i
                beginning = False
        elif i in '?.!':
            beginning = True
            new_str += i
        else:
            new_str +=i
    return new_str, count

def replace_punctuation(usr_str, exclamation_count=0, semicolon_count=0):
    new_str= ''
    for character in usr_str:
        if character == '!':
            new_str += '.'
            exclamation_count +=1
        elif character == ';':
            new_str += ','
            semicolon_count +=1
        else:
            new_str += character
    return new_str


def shorten_space(usr_str):
    while '  ' in usr_str:
        usr_str = usr_str.replace('  ', ' ')
    return usr_str

if __name__ == '__main__':
    # Complete main section of code
    user_string = str(input('Enter a sample text:\n'))
    print('\nYou entered:', user_string)
    
    print_menu(user_string)
    
