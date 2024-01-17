import math

def findFact(n):
    if (n == 1):
        return n
    return n * findFact(n - 1)

def generateFib(n):
    t1 = 0
    t2 = 1
    t3 = 0
    print(t1)
    print(t2)
    while(n-2):
        t3 = t1 + t2
        t1 = t2
        t2 = t3
        print(t3)
        n -= 1

# def isPrime(num):
#     prime = [True for i in range(num + 1)]
#     p = 2
#     while (p * p <= num):
#         if (prime[p] == True):
#             for i in range(p * p, num + 1, p):
#                 prime[i] = False
#         p += 1

#     for p in range(2, num + 1):
#         if prime[p]:
#             print(p)

def isPrime(n):
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0: 
            return False
    return True

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
                n = int(input("Enter n..."))
                print(findFact(n))
            case 2:
                n = int(input("Enter number of terms..."))
                generateFib(n)
            case 3:
                n = int(input("Enter number..."))
                print(isPrime(n))
            case 0:
                print("Exiting...")
                ans = False
            case _:
                print("Invalid choice...")

def main():
    runMenu()

if __name__ == "__main__":
    main()
