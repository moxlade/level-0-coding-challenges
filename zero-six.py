def maxi_number(x,y,z):
    if x > y and x > z:
        return x
    elif y > x and y > z:
        return y
    else:
        return z 

a = int(input())
b = int(input())
c = int(input())
print(maxi_number(a,b,c))
