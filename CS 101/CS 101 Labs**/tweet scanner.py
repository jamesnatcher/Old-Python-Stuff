tweet = str(input('Enter tweet:\n'))
print('Tweet:', tweet)

word_dict = {'LOL': 'LOL =laughing out loud',
             'BFN': 'BFN = bye for now',
             'FTW': 'FTW = for the win',
             'IRL': 'IRL = in real life',
             'LBJ': 'LBJ = Lebron James',}
             
if tweet in word_dict:
    print('\nAbbreviations:')
    if 'LOL' in tweet:
        print(word_dict['LOL'])
    if 'BFN' in tweet:
        print(word_dict['BFN'])
    if 'FTW' in tweet:
        print(word_dict['FTW'])
    if 'IRL' in tweet:
        print(word_dict['IRL'])
    if 'LBJ' in tweet:
        print(word_dict['LBJ'])
    
