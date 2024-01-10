def max_of_three(a, b, c): 
    if (a > b & a > c):
        return a
    elif (b > a & b > c):
        return b
    else:
        return c

a = int(input("Enter first: "))
b = int(input("Enter second: "))
c = int(input("Enter third: "))
print(max_of_three(a, b, c))

def area(l, b):
    return l*b

l = int(input("Enter length: "))
b = int(input("Enter breadth: "))

print(area(l, b))


