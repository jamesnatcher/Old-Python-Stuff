morse_code = { 'A' : ".- ",
               'B' : "-... ", 
               'C' : "-.-. ",
               'D' : "-.. ",
               'E' : ". ", 
               'F' : "..-. ",
               'G' : "--. ",
               'H' : ".... ", 
               'I' : ".. ",
               'J' : ".--- ",
               'K' : "-.- ", 
               'L' : ".-.. ",
               'M' : "-- ",
               'N' : "-. ", 
               'O' : "--- ",
               'P' : ".--. ",
               'Q' : "--.- ", 
               'R' : ".-. ",
               'S' : "... ",
               'T' : "- ", 
               'U' : "..- ",
               'V' : "...- ",
               'W' : ".-- ", 
               'X' : "-..- ",
               'Y' : "-.-- ",
               'Z' : "--.. ",
               '0' : "----- ",
               '1' : ".---- ",
               '2' : "..--- ",
               '3' : "...-- ", 
               '4' : "....- ",
               '5' : "..... ",
               '6' : "-.... ", 
               '7' : "--... ",
               '8' : "---.. ",
               '9' : "----. ", 
               ' ' : "  "
}

user_text = input('Please enter a line of text \n')
clear_text = ''

for c in user_text:
    if (ord('A') <= ord(c)) and (ord(c) <= ord('Z')):
        mod = c 
    elif (ord('a') <= ord(c)) and (ord(c) <= ord('z')):
        mod = chr((ord(c) - ord('a')) + ord('A'))
    elif c in '!&:;\',.?':
        continue
    else:
        mod = c 
    clear_text += mod
print('\nTransmitting\n', clear_text)

count = 0
for c in clear_text:
    print(morse_code[c], end='')
    for i in morse_code[c]:
        count += 1
        if count >= 40 and i == ' ':
            count = 0
            print('\n')
    
