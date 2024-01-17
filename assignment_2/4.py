def main(): 
    # To count number of words
    count = 0
    with open("tmp.txt","r+") as file:
        data = file.read()
        lines = data.split()
        for i in range(len(lines)):
            print(lines[i])
            
        for word in lines:
            if not word.isnumeric(): # counts only words, not numbers
                count += 1
    
    print("Count:", count)

    # Copying file
    file_copy = open("tmp_copy.txt", "w+")
    with open("tmp.txt","r+") as file:
        data = file.readlines()
        for i in range(len(data)):
            file_copy.write(data[i])
    print("Contents of file successfully copied!")

    


if __name__=="__main__": 
    main() 