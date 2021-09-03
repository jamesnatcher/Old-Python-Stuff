string_list = []
int_list = [] 

#get title and column titles
data_title = input('Enter a title for the data:\n')
print('You entered: {}\n'.format(data_title))
column_1_header = input('Enter the column 1 header:\n')
print('You entered: {}\n'.format(column_1_header))
column_2_header = input('Enter the column 2 header:\n')
print('You entered: {}\n'.format(column_2_header))

#data inputting here
def data_entry():
    data_points = input('Enter a data point (-1 to stop input):\n')
    while data_points != '-1':
        string_split = data_points.split(',')
        string_raw = string_split[0].strip()
        num_string = ''.join(data_points.split())
        num_raw = num_string.split(',')
        if ',' not in data_points:
            print('Error: No comma in string.\n')
        elif data_points.count(',') > 1:
            print('Error: Too many commas in input.\n')
        elif not num_raw[1].isdigit():
            print('Error: Comma not followed by an integer.\n')
        else:
            print('Data string:', string_raw)
            string_list.append(string_raw)
            print('Data integer: {}\n'.format(num_raw[1]))
            int_list.append(num_raw[1])
        data_points = input('Enter a data point (-1 to stop input):\n')
data_entry()

#table
def table(stringlist, intlist):
    print('\n{title:^44}'.format(title=data_title))
    print('{column1:<20}|{column2:>23}'.format(column1=column_1_header, column2=column_2_header))
    print('-'*44)
    for i in range(len(stringlist)):
        print('{:<20}|{:>23}'.format(stringlist[i], intlist[i]))
table(string_list, int_list)

#histogram
def histo(stringlist, intlist):
    print()
    for i in range(len(stringlist)):
            print('{:>20}'.format(stringlist[i]), end=' ')
            print('*' * int(intlist[i]))
histo(string_list, int_list)

