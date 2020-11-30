def my_function(x,y):

    mySum = x + y    

    if x == 3 or y == 3 and "3" in str(mySum) :
        return True
    
    else:
        return False

print(my_function(3,10))
