def mad_lib(thing_list):
    while 'quit' not in thing_list:
        print('Eating {second} {first} a day keeps the doctor away.'.format(first=thing_list[0], second=thing_list[1]))
        thing_list = input().split()

thing_list = input().split()
mad_lib(thing_list)
