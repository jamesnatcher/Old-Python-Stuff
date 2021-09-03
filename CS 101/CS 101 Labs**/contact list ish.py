rawcontacts = list(input().split())
contact_list = {}

for i in rawcontacts[::2]:
    contact_list[i] = rawcontacts[rawcontacts.index(i)+1]

desiredcontact = input()

print(contact_list[desiredcontact])
