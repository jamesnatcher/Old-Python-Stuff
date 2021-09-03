    user_text = input()
number_overall = len(user_text)

for character in user_text:
    if character == ' ':
        number_overall -= 1
    elif character == '.':
        number_overall -= 1
    elif character == ',':
        number_overall -= 1
print(number_overall)
