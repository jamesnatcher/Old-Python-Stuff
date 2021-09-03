
def fibon(n):

    num = 1
    prevNum = 0
    sumbudy = 0
    
    for x in range(n-1):
        
        sumbudy = num + prevNum
        prevNum = num
        num = sumbudy

    return sumbudy

        

        
