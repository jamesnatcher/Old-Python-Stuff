def add_player(team):
    new_jersey = int(input('\nEnter a new playe\'s jersey number:'))
    new_rating = int(input('\nEnter the player\'s rating:'))
    team[new_jersey] = new_rating

def remove_player(team):
    remove_jersey = int(input('\nEnter a jersey number:'))
    if remove_jersey in team:
        del team[remove_jersey]
    
def update_rating(team):
    jersey = int(input('\nEnter a jersey number:'))
    new_rating = int(input('\nEnter a new rating for player:'))
    team[jersey] = new_rating
    
def output_above_rating(team):
    sorted_list = []
    rating = int(input('\nEnter a rating:'))
    for key in team:
        if team[key] >= rating:
            sorted_list.append(key)
    sorted_list.sort()
    print('\nABOVE {}'.format(rating))
    for i in sorted_list:
        print('Jersey number: {}, Rating: {}'.format(i, team[i]))        
    
def output_roster(team):
    sorted_jersey = list(team.keys())
    sorted_jersey.sort()
    print('\nROSTER')
    for i in sorted_jersey:
        print('Jersey number: {}, Rating: {}'.format(i, team[i]))
    


if __name__== "__main__":
    team = dict()
    loop = True
    while loop:
        print('\nMENU\na - Add player\nd - Remove player\nu - Update player rating\nr - Output players above a rating\no - Output roster\nq - Quit')
        user_choice = input('\nChoose an option:')
        if user_choice == 'a':
            add_player(team)
        elif user_choice == 'd':
            remove_player(team)
        elif user_choice == 'u':
            update_rating(team)
        elif user_choice == 'r':
            output_above_rating(team)
        elif user_choice == 'o':
            output_roster(team)
        elif user_choice == 'q':
            loop = False
