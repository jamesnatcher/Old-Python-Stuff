desire = input("Enter desired auto service:\n")
service = {'Oil change': 35, 'Tire rotation': 19, 'Car wash': 7}
print('You entered:', desire)
if desire in service:
    if desire == 'Oil change':
        print('Cost of oil change: ${}'.format(service.get(desire)))
    if desire == 'Tire rotation':
        print('Cost of tire rotation: ${}'.format(service.get(desire)))
    if desire == 'Car wash':
        print('Cost of car wash: ${}'.format(service.get(desire)))
else: 
    print('Error: Requested service is not recognized')
