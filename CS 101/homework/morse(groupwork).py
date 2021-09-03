# Paul James Natcher and Vincent Sereyko

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
               'X' : "-..-",
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

morse_text = {}

def filter_morse(text):
    new_text = ''
    for c in text:
        if c in '.- ':
            new_text += c
    return new_text
    
def tokenize_morse(text):
    l = []
    buffer = ''
    for morse in text:
        if morse != ' ':
            buffer += morse
        else:
            l.append(buffer)
            buffer = ''
    if buffer != '':
        l.append(buffer)
    return l
        
def revert_morse_code_dictionary(morse):
    for key in morse_code:
        morse_text[morse_code[key]] = key
    return morse_text
    
def decode_tokenized_morse(l): 
    revert_morse_code_dictionary(morse_code)
    translated = ''
    for morse in l:
        if morse == "":
            translated += morse_text['  ']
        else:
            translated += morse_text[morse + ' ']
    return translated
    
def decode_morse(text):
    return decode_tokenized_morse(tokenize_morse(filter_morse(text)))


if __name__ == "__main__":
    cont = True
    while cont:
        text = input("Please enter a line of morse code text. Enter an empty line to stop.\n")
        if text != "":
            print(decode_morse(text))
        else:
            cont = False

            
            
