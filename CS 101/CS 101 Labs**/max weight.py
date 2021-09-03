person_1 = input("Enter the 1st person's name")
person_1_weight = int(input("Enter the 1st person's weight in lbs"))

person_2 = input("Enter 2nd person's name")
person_2_weight = int(input("Enter the 2nd person's weight in lbs"))

person_3 = input("Enter 3rd person's name")
person_3_weight = int(input("Enter the 3rd person's weight in lbs"))

person_4 = input("Enter 4th person's name")
person_4_weight = int(input("Enter the 4th person's weight in lbs"))

max_weight = person_1_weight
max_name = person_1
if person_2_weight > max_weight:
    max_weight = person_2_weight
    max_name = person_2
if person_3_weight > max_weight:
    max_weight = person_3_weight
    max_name = person_3
if person_4_weight > max_weight:
    max_weight = person_4_weight
    max_name = person_4


print("The heaviest person is {}. They weigh {} lbs.".format(max_name, max_weight))
