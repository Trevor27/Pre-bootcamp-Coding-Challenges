def my_function():
    x = int(input("Enter a number: "))
    y = int(input("Enter a number: "))

    mySum = x + y    

    if x == 3 or y == 3 and "3" in str(mySum) :
        return True
    
    else:
        return False

print(my_function())
