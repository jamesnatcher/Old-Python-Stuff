#################################################################
#
#  Paul James Natcher
#
#################################################################

# Points possible: 5
def average_of_list_elements(l):
    if len(l) == 0:
        return 0.0
    s = 0
    for i in l:
        s += float(i)
    a = s / len(l)
    return a


# Points possible: 5
def list_without_repetitions(l): 
    new_l = []
    for i in l:
        if i not in new_l:
            new_l.append(i)
    return new_l
    

# Points possible: 10
def list_to_list_of_occurrences(l):
    occurences = dict()
    for i in l:
        if i in occurences:
            occurences[i] += 1
        else:
            occurences[i] = 1
    tuples = []
    for i in occurences:
        tuples.append((i, occurences[i]))
    return tuples
    

# Points possible: 12
def is_permutation_list(l1, l2):
    if len(l1) != len(l2):
        return False
    
    occurences1 = dict()
    occurences2 = dict()

    for i in l1:
        if i in occurences1:
            occurences1[i] += 1
        else:
            occurences1[i] = 1
            
    for i in l2:
        if i in occurences2:
            occurences2[i] += 1
        else:
            occurences2[i] = 1
            
    for i in occurences1.keys():
        if i not in occurences2.keys():
            return False
        elif occurences1[i] != occurences2[i]:
            return False
    
    return True

            
