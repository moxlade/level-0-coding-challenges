
def triangle_area(x,y,z):
    s = 0.5 * (x + y +z)
    h = s*(s-x)*(s-y)*(s-z)
    a = h ** 0.5
    return a

f = int(input())
g = int(input())
j = int(input())
print(triangle_area(f,g,j))

