def initial_of_name(name):
    parts = name.split()
    i = len(parts)-1
    new_list = []
    for j in range(0,i):
        part = parts[j]
        part = part[0:1]
        new_list.append(part + '.')
    new_list.append(parts[-1])
    return new_list

name = input('Enter the name to be turned into its initials: ')
final_list = initial_of_name(name)
print('{},'.format(final_list[-1]), end=' ')
for k in range(len(final_list)-1):
    print('{}'.format(final_list[k]), end='')
print()
