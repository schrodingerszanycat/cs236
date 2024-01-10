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

def area(arg):
    if (arg == 1):
        r = int(input("Enter radius: "))
        return r*r
    elif (arg == 2):
        l = int(input("Enter length: "))
        b = int(input("Enter breadth: "))
        return l*b


arg = int(input("Enter 1 circle, 2 for rectangle"))
print(area(arg))


