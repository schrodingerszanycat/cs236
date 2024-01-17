def findFact():


def generateFib():


def isPrime():

    
def runMenu():
    ans = True
    while ans:
        print("\nMENU")
        print("1 - Calculates factorial of a given number.")
        print("2 - Generates Fibonacci sequence up to a specified term.")
        print("3 - Checks if a number is prime.")
        print("0 - Exit")

        choice = int(input("Enter choice..."))
        match choice:
            case 1:
                number = int(input("Enter number..."))
                print(findFact(number))
            case 2:
                number = int(input("Enter number of terms..."))
                generateFib(number)
            case 3:
                number = int(input("Enter number..."))
                print(isPrime(number))
            case 0: 
                print("Exiting...")
                ans = False
            case _:
                print("Invalid choice...")
        
def main(): 
    runMenu()

if __name__=="__main__": 
    main() 