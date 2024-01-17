def main(): 
    tuple1 = ("APPLE", 1, True, "Banana")
    print(tuple1)

    text = "AI Lab"
    tuple2 = (text,) * 3
    print(tuple2)

    tuple3 = tuple1 + tuple2
    print(tuple3)

if __name__=="__main__": 
    main() 