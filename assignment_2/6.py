def main(): 
    keys = ["Ten", "Twenty", "Thirty"] 
    values = [10, 20, 30]
    
    dict = {}
    for i in range(len(keys)):
        dict[keys[i]] = values[i]
    
    print(dict)

if __name__=="__main__": 
    main() 