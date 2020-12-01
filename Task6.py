def max_num(x,y,z):
    if x > (y and z):
        return x
    elif y > (x and z):
        return y
    else:
        return z
print(max_num(4,5,6))
