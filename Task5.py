
def area_of_triangle(a,b,c):
    s = (1/2)*(a + b + c)
    z = s*(s - a)*(s - b)*(s - c)
    area = (z)**(1/2)
    return area
print(area_of_triangle(4,5,6))
