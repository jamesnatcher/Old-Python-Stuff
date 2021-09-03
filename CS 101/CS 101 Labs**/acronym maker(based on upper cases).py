def acronyms(string):
    acro = ''
    for char in string:
        if char.isupper():
            acro += char
    print(acro)
      
usr_str = input()
acronyms(usr_str)
