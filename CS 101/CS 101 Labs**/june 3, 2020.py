'''rawtext = input('Enter the text to be encoded with the Cesar cypher: ')
shift = int(input('Enter the Cesar cypher shift amount: '))

cleartext = ''

for c in rawtext:
    if ((ord('A') <= ord((c)) and (ord(c)) <= ord('Z'))):
        m = c
    elif ((ord('a') <= ord((c)) and (ord(c)) <= ord('z'))):
        m = chr(ord(c) - ord('a') + +ord('A'))
    else:
        m = ''
    cleartext += m

print('The cleartext to be encoded is \"{}\"'.format(cleartext))

cyphertext = ''
for c in cleartext:
    p = ord(c) - ord('A')
    p = (p+shift) % 26
    m = chr(p + ord('A'))
    cyphertext +=m

print('The cyphertext with the shift {} is \"{}\"'.format(shift, cyphertext))'''

################################################################################

