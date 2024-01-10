def max_of_three(a, b, c): 
    if (a > b & a > c):
        print(a, "is the maximum.")
    elif (b > a & b > c):
        print(b, "is the maximum.")
    else:
        print(c, "is the maximum.")

a = int(input("Enter first: "))
b = int(input("Enter second: "))
c = int(input("Enter third: "))
max_of_three(a, b, c)

def area(l, b):
    return l*b

l = int(input("Enter length: "))
b = int(input("Enter breadth: "))

print(area(l, b))


