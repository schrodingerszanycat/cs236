def countWords(filename):
    n_word = 0
    n_line = 0
    n_spaces = 0
    with open(filename, "r+") as f:
        d = f.readlines()
        n_line = len(d)
    with open(filename, "r+") as file:
        data = file.read()
        for x in data: 
            if x == " ":
                n_spaces += 1
        lines = data.split()
        #print(lines)
        for word in lines:
            if not word.isnumeric(): 
                n_word += 1
    print("Word count:", n_word)
    print("Line count: ", n_line)
    print("space count: ", n_spaces)

def countUnique(filename):
    unique = set()
    with open(filename, "r+") as file:
        data = file.read()
        lines = data.split()
        #print(lines)
        for word in lines:
            if not word.isnumeric(): 
                unique.add(word)
    print(len(unique))

def displayFreq(filename):
    words = {}
    with open(filename, "r+") as file:
        data = file.read()
        lines = data.split()
        #print(lines)
        for word in lines:
            if not word.isnumeric(): 
                words[word] = 0
        for word in lines:
            if not word.isnumeric(): 
                words[word] += 1
    for word in words:
        print(word, words[word])
        
def displayLongest(filename):
    with open(filename, "r+") as file:
        data = file.read()
        words = data.split()
        longest_word = max(words, key=len)
        print("Longest word:", longest_word)

def displayAvgLength(filename):
    with open(filename, "r+") as file:
        data = file.read()
        words = data.split()
        print(words)
        total_length = sum(len(word) for word in words)
        avg_length = total_length / len(words)
        print("Average length of words:", avg_length)

def displaySimilarity(filename):
    with open(filename, "r+") as file:
        data = file.readlines()
        line1, line2 = data[0], data[1]
        d1, d2 = line1.split(), line2.split()
        l, c = min(len(d1), len(d2)), 0
        #print(d1, d2)
        for w1 in d1: 
            for w2 in d2:
                if w1 == w2: c += 1
        if (c >= l/2): print("1")
        else: print("0")

def runMenu():
    ans = True
    filename1 = input("Enter filename: ")
    while ans:
        print("\nMENU")
        print("1. Count words, lines, spaces")
        print("2. Count unique words")
        print("3. Display frequency of each word")
        print("4. Display longest word")
        print("5. Display average length of words")
        print("6. Compare similarity")
        print("0. Exit")
        c  = int(input("Enter choice: "))
        if c == 1:
            countWords(filename1)
        elif c == 2:
            countUnique(filename1)
        elif c == 3:
            displayFreq(filename1)
        elif c == 4:
            displayLongest(filename1)
        elif c == 5:
            displayAvgLength(filename1)
        elif c == 6:
            displaySimilarity(filename1)
        elif c == 0:
            print("Exiting...")
            ans = False
        else:
            print("Invalid choice.")
        
def main():
	runMenu()

if __name__ == '__main__':
	main()
	