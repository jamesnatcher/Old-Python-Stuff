highway_number = int(input())

if (highway_number == 0) or (highway_number % 100 == 0):
    print('{} is not a valid interstate highway number.'.format(highway_number)) 
if highway_number > 999:
    print('{} is not a valid interstate highway number.'.format(highway_number)) 
if highway_number > 0 and highway_number < 100:
    if (highway_number % 2) == 0:
        print('I-{} is primary, going east/west.'.format(highway_number))
    else:
        print('I-{} is primary, going north/south.'.format(highway_number))
if highway_number > 99 and highway_number < 1000:
    if highway_number % 100 == 0:
        print()
    else:
        if (highway_number % 2) == 0:
            if_aux = highway_number % 100
            print('I-{} is auxiliary, serving I-{}, going east/west.'.format(highway_number, if_aux))
        else:
            if_aux = highway_number % 100
            print('I-{} is auxiliary, serving I-{}, going north/south.'.format(highway_number, if_aux))
