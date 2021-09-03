#################################################################
#
#  Paul James Natcher
#
#################################################################

# Points possible: 5
def mirror_string(s):
    clist = []
    for c in s:
        clist.append(c)
    string = ''
    inverse_count = -1
    for c in range(len(clist)):
        string += clist[inverse_count]
        inverse_count -= 1
    return string


# Points possible: 6
def make_palindrome(s):
    reverse = mirror_string(s)
    s += reverse
    return s


# Points possible: 8
def is_palindrome(s):
    left = 0
    right = len(s) -1
    while (left < right):
        if s[left] != s[right]:
            return False
        elif s[left] == s[right]:
            left += 1
            right -= 1
    return True


# Points possible: 10
def string_to_dict(s):
    sdict = dict()
    for i in range(len(s)):
        if s[i] in sdict:
            sdict[s[i]].append(i)
        else:
            sdict[s[i]] = [i]
    
    return sdict
    

# Points possible: 12
def dict_to_string(d):
    if len(d) == 0:
        return ''
    maximum = 0
    for k1, v1 in d.items():
        for v in v1:
            if v >= maximum:
                maximum = v
    l = [' ' for i in range(maximum + 1)]
    for k, v in d.items():
        for i in v:
            l[i] = k
    string = ''
    for i in l:
        string += i
    
    return string

