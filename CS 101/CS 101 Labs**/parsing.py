def parser():
    string = input("Enter input string:")
    while string != ("q"):
        new = [] 
        if ',' in string:
            old = string.split(',')
            for word in old:
                word = word.replace(' ','')
                new.append(word)
            print('\nFirst word: {:<}\nSecond word: {:<}'.format(new[0], new[-1]))
        elif ',' not in string:
            print('\nError: No comma in string.')
        string = input("\nEnter input string:")
    print()
        

parser()
