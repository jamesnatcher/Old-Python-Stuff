def palindrome_check(string, string_mod):
    if string_mod[::1] == string_mod[::-1]:
        print(string, 'is a palindrome')
    else: 
        print(string, 'is not a palindrome')
    
    
usr_str = input()
usr_str_mod = ''.join(usr_str.split())
palindrome_check(usr_str, usr_str_mod)
