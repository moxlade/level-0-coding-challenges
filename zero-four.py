def even_or_odd(x):
    if x % 2 == 0:
        return "even"
    else:
        return "odd"

y = int(input())
print(even_or_odd(y))
