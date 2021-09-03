print('Davy\'s auto shop services\nOil change -- $35\nTire rotation -- $19\nCar wash -- $7\nCar wax -- $12\n')


service = {'Oil change': 35, 'Tire rotation': 19, 'Car wash': 7, 'Car wax': 12}
no_service = {'-': 0}

first_service = input('Select first service:')
second_service = input('Select second service:')

print('\nDavy\'s auto shop invoice\n')
if first_service in service:
    print('Service 1: {}, ${}'.format(first_service, service.get(first_service)))
elif first_service == '-':
    print('Service 1: No service')
if second_service in service:
    print('Service 2: {}, ${}'.format(second_service, service.get(second_service)))
elif second_service == '-':
    print('Service 2: No service')
if first_service in service:
    service1_cost = int((service.get(first_service)))
else:
    service1_cost = 0
if second_service in service:
    service2_cost = int((service.get(second_service)))
else: 
    service2_cost = 0
total = service1_cost + service2_cost
print('\nTotal: ${}'.format(total))
