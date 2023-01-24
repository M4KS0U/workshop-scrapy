for num in range(1, 100) :
    print(num)
    if (num % 3 == 0 and num % 5 == 0) :
        print("ThreeFive")
    elif (num % 3 == 0) :
        print("Three")
    elif (num % 5 == 0) :
        print("Five")