def OptimalArea(Increment):
    TotalFence = 600
    x=0
    Len = x
    Len2 = TotalFence - 2*x
    Area = Len * Len2
    ListOfValues = []
    while 2*x < TotalFence:

        ListOfValues.append(Area)
        Len=x
        Len2=TotalFence-2*x
        x = x+Increment
        Area = Len*Len2
    
        while True:

            if all(q < Area for q in ListOfValues) == False:
                break

            else:
                print(">>> Current Largest:  ", Area)
                print("Side Length 1:  ", round(Len, 1))
                print("Side Length 2 : ", Len2)
                print("")
                break

    print(" ")
    print("The Max Area:", max(ListOfValues))
    print("")

OptimalArea(5)
