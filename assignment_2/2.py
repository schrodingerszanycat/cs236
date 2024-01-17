import math

def findArea():
    radius = int(input("Enter radius..."))
    area = math.pi * radius * radiusimport math

def findArea():
    radius = int(input("Enter radius..."))
    area = math.pi * radius * radius
    print("Area: ", round(area, 2))

def checkOddity():
    number = int(input("Enter number..."))
    if (number % 2 == 0):
        print(number, " is even")
    else: 
        print(number, " is odd")

def convertTemp():
    print("Enter 0 for Celsius to Fahrenheit conversion, 1 for vice versa")
    number = int(input("Enter number..."))
    temp = int(input("Enter temperature..."))
    match number:
        case 0:
            fahrenheit = (1.8 * temp) + 32
            print(temp, " in Celsius is ", fahrenheit, " in Fahrenheit")
        case 1:
            celsius = ((temp - 32) * 5) / 9
            print(temp, " in Fahrenheit is ", celsius, " in Celsius")
        case _:
            print("Invalid choice...")            

def runMenu():
    ans = True
    while ans:
        print("\nMENU")
        print("1 - Find the area of a circle given its radius.")
        print("2 - Check if a given number is even or odd.")
        print("3 - Convert temperature from Celsius to Fahrenheit and vice versa.")
        choice = int(input("Enter choice..."))
        match choice:
            case 1:
                findArea()
            case 2:
                checkOddity()
            case 3:
                convertTemp()
            case 0: 
                ans = False
            case _:
                print("Invalid choice...")
        
def main(): 
    runMenu()

if __name__=="__main__": 
    main() 
    print("Area: ", round(area, 2))

def checkOddity():
    number = int(input("Enter number..."))
    if (number % 2 == 0):
        print(number, " is even")
    else: 
        print(number, " is odd")

def convertTemp():
    print("Enter 0 for Celsius to Fahrenheit conversion, 1 for vice versa")
    number = int(input("Enter number..."))
    temp = int(input("Enter temperature..."))
    match number:
        case 0:
            fahrenheit = (1.8 * temp) + 32
            print(temp, " in Celsius is ", fahrenheit, " in Fahrenheit")
        case 1:
            celsius = ((temp - 32) * 5) / 9
            print(temp, " in Fahrenheit is ", celsius, " in Celsius")
        case _:
            print("Invalid choice...")            

def runMenu():
    ans = True
    while ans:
        print("MENU")
        print("1 - Find the area of a circle given its radius.\n")
        print("2 - Check if a given number is even or odd.\n")
        print("3 - Convert temperature from Celsius to Fahrenheit and vice versa.\n")
        choice = int(input("Enter choice..."))
        match choice:
            case 1:
                findArea()
            case 2:
                checkOddity()
            case 3:
                convertTemp()
            case 0: 
                ans = False
            case _:
                print("Invalid choice...")
        
def main(): 
    runMenu()

if __name__=="__main__": 
    main() 