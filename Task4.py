def threeInSum(x,y):
    mySum = x + y    
    if (x == 3 or y == 3) and "3" in str(mySum) :
        return True
    else:
        return False
print(threeInSum(3,10))
