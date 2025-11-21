for i in range (1, 26):
    if i % 2 == 0:
        if len(str(i / 2)) == 2:
            print(int(i / 2 ), end="  ")
        else:
            print(str(int(i / 2 )), end= "  ")
    else:
        print ("*", end="  ")
        if i % 5 == 0:
            print()