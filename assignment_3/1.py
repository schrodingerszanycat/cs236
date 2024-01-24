def read_data(filepath):
    l = []
    with open(filepath, "r") as file:
        data = file.readlines()
        for line in data:
            parts = line.strip().split(", ")
            if len(parts) == 3:
                entry = {
                    "ID": int(parts[0]),
                    "Name": parts[1],
                    "Age": int(parts[2])
                }
                l.append(entry)
    return l

def write_data(filepath, data):
    with open(filepath, 'w') as file:  
        for record in data:
            for key, value in record.items():  
                file.write('%s:%s\n' % (key, value))
            file.write("\n")

    print("Data written into", filepath, "successfully!")

def update_age(filepath, person_id, new_age):
    with open(filepath, "r") as file:
        data = file.readlines()

    updated_data = []
    for line in data:
        parts = line.strip().split(", ")
        if len(parts) == 3 and int(parts[0]) == person_id:
            parts[2] = str(new_age)
        updated_data.append(", ".join(parts))

    with open(filepath, "w") as file:
        file.writelines('\n'.join(updated_data))

def main():
    # Creating file
    filepath = "data.txt"
    file = open(filepath, "w+")
    L = ["1, John, 25 \n",
         "2, Jane, 30 \n",
         "3, Bob, 22 \n",
         "4, Alice, 28 \n"]
    file.writelines(L)
    file.close()

    # Reading from file
    lst = read_data(filepath)
    print(lst)

    # Writing onto file
    filepath_new = "data_cpy.txt"
    write_data(filepath_new, lst)

    # Updating file
    new_age = 40
    id = 1
    update_age(filepath, id, new_age)
if __name__ == "__main__":
    main()





