def my_function():
    x = int(input("Enter a number: "))
    y = int(input("Enter a number: "))

    if x == 65 or y == 65 or (x + y) == 65:
        return True
    
    else:
        return False

 
print(my_function())
