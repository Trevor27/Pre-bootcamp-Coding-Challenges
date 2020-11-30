def max_num(x,y,z):

    if x > (y and z):
        print(x)

    elif y > (x and z):
        print(y)

    else:
        print(z)

max_num(4,5,6)
