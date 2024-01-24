def process_data(input, output):
    with open(output, "w") as file2:
        with open(input, "r") as file1:
            data = file1.readlines()
            for line in data:
                numbers = line.strip().split(", ")
                for number in numbers:
                    file2.write(str(int(number)**2))
                    file2.write(", ")
                file2.write("\n")
    
    print("Numbers squared successfully!")

def main():
    input_filename = "infile.txt"
    output_filename = "outfile.txt"

    process_data(input_filename, output_filename)

if __name__ == "__main__":
    main()





