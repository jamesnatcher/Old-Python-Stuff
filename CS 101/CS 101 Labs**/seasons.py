month_length = {'January': 31,
                'February': 29,
                'March': 31,
                'April': 30,
                'May': 31,
                'June': 30,
                'July': 31,
                'August': 31,
                'September': 30,
                'October': 31,
                'November': 30,
                'December': 31}
                
if input_month in month_length:
    last_day = month_length[input_month]
    if (input_day <= last_day) and (input_day > 0):
        if (input_month == 'January') or (input_month == 'February') or (input_month == 'March' and input_day <= 19) or  (input_month == 'December' and input_day >= 21):
            print('Winter')
        elif (input_month == 'April') or (input_month == 'May') or (input_month == 'June' and input_day <= 20) or (input_month == 'March' and input_day >= 20):
            print('Spring')
        elif (input_month == 'July') or (input_month == 'August') or (input_month == 'September' and input_day <= 21) or (input_month == 'June' and input_day >= 21):
            print('Summer')
        elif (input_month == 'October') or (input_month == 'November') or (input_month == 'December' and input_day <= 20) or (input_month == 'September' and input_day >= 22):
            print('Autumn')
            
    else:
        print('Invalid')
else:
    print('Invalid')
    
    
