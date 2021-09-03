
def lookup_in_list(li, e):
    '''Assumes that list is sorted'''
    l = 0
    r = len(li) - 1
    while l < r:
        m = (l + r) // 2
        if li[m] == e:
            return m
        if li[m] < e:
            l = m + 1
        else:
            r = m - 1
    return -1


def lookup_in_unsorted_list(li, e):
    '''List l is not sorted'''
    for i in range(len(l)):
        if li[i] == e:
            return i
    return -1 
        
