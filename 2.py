def print_unique(lst):
    elements = set()
    for x in lst:
        elements.add(x)
    print("The unique entries are: ")
    for element in elements:
        print(element)

lst = []
n = int(input("Enter number of elements : "))

for i in range(0, n):
    ele = int(input())
    lst.append(ele)  

print_unique(lst)
 