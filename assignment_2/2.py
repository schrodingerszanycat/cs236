import math

def revStr(string):
    return string[::-1]

def countVowels(string):
    vowels = "AEIOUaeiou"
    count = len([char for char in string if char in vowels])
    return count

def isPalindrome(string):
    reversed_string = revStr(string)
    if (string != reversed_string):
        return False
    return True

def runMenu():
    ans = True
    while ans:
        print("\nMENU")
        print("1 - Reverse a given string.")
        print("2 - Count the number of vowels in a given string.")
        print("3 - Checks if a given word is a palindrome.")
        print("0 - Exit")
        choice = int(input("Enter choice..."))
        match choice:
            case 1:
                string = input("Enter string...")
                revStr(string)
            case 2:
                string = input("Enter string...")
                countVowels(string)
            case 3:
                string = input("Enter string...")
                isPalindrome(string)
            case 0: 
                print("Exiting...")
                ans = False
            case _:
                print("Invalid choice...")
        
def main(): 
    runMenu()

if __name__=="__main__": 
    main() 