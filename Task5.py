import math 

def area_of_triangle():
    a = int(input("enter 1st side length of the triangle: "))
    b = int(input("enter 2nd side length of the triangle: "))
    c = int(input("enter 3rd side length of the triangle: "))

    s = (1/2)*(a + b + c)
  
    z = s*(s - a)*(s - b)*(s - c)

    area = math.sqrt(z)
    
    print("The area of the triangle is: "+ str(area))

area_of_triangle()
