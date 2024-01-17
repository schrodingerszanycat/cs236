import math

def sum(lst):
    result = 0
    for x in range(0, len(lst)):
        result += lst[x]
    return result
    # return sum(lst)

def findLargest(lst):
    if (len(lst) == 0):
        return "List empty"
    # max = lst[0]
    # for x in range(0, len(lst)):
    #     if (lst[x] > max):
    #         max = lst[x]
    # return max
    return max(lst)

def removeDup(lst):
    elements = set()
    for x in lst:
        elements.add(x)
    return elements
    
def runMenu():
    ans = True
    # Taking list as input
    lst = []
    n = int(input("Enter number of elements : "))
    for i in range(0, n):
        ele = int(input())
        lst.append(ele) 

    while ans:
        print("\nMENU")
        print("1 - Find the sum of all elements in a list.")
        print("2 - Find the largest element in a list.")
        print("3 - Remove duplicates from a list.")
        print("0 - Exit")

        choice = int(input("Enter choice from menu..."))
        match choice:
            case 1:
                print(sum(lst))
            case 2:
                print(findLargest(lst))
            case 3:
                print(removeDup(lst))
            case 0: 
                print("Exiting...")
                ans = False
            case _:
                print("Invalid choice...")
        
def main(): 
    runMenu()

if __name__=="__main__": 
    main() 