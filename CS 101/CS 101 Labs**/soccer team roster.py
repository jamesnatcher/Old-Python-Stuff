num_and_ratings = {}
sorted_jersey = []

initialcount = 0
for initialcount in range(5):
    jersey_num = int(input('Enter player {}\'s jersey number:'.format(initialcount + 1)))
    rating_num = int(input('Enter player {}\'s rating:'.format(initialcount + 1)))
    num_and_ratings[jersey_num] = rating_num
    sorted_jersey.append(rating_num)
    print()
    initialcount += 1

sorted_jersey.sort()

print('ROSTER')
for num in sorted_jersey:
    print('Jersey number: {}, Rating: {}'.format(num, num_and_ratings[num]))
print()

menu = 'MENU\na - Add player\nd - Remove player\nu - Update player rating\nr - Output players above a rating\no - Output roster\nq - Quit\n\nChoose an option:'
print(menu)
user_input = input()

while user_input != 'q':
    if user_input == 'o':
        print('\nROSTER')
        for num in sorted_jersey:
            sorted_jersey.sort()
            print('Jersey number: {}, Rating: {}'.format(num, num_and_ratings[num]))
        print()
    if user_input == 'a':
        jersey_new = int(input('Enter a new player\'s jersey number:'))
        rating_new = int(input('Enter the player\'s rating:'))
        num_and_ratings[jersey_new] = rating_new
        sorted_jersey.append(rating_new)
        sorted_jersey.sort()
        print(num_and_ratings)
    if user_input == 'd':
        jersey_del = int(input('Enter a jersey number:'))
        del num_and_ratings[jersey_del]
        sorted_jersey.remove(jersey_del)
        print()
    if user_input == 'u':
        print('u')
    if user_input == 'r':
        print('r')
    print(menu)
    user_input = input()



    
