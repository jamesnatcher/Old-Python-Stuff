import math

def square_root(x):
    '''y ** 2 - x == 0'''
    if x == 0.0:
        return x
    l = 0.0
    if x > 1.0:
        r = x
    else:
        r = 1.0
    while (r !=l):
        print('sqrt{} must be betweeen {} and {}'.format(x, l, r))
        m = (l + r) / 2
        m_squared = m * m
        if m_squared < x:
            if l == m:
                break
            l = m
        else:
            if r == m:
                break
            r = m
        
    y = (l + r)/2
    return y

if __name__ == "__main__":
    
    x = float(input('Enter a positive or zero number '))
    print(square_root(x))
    print(math.sqrt(x))


