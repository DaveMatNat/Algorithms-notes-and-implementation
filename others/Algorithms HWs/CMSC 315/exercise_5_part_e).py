def ReadInput():
    #inputs
    C=[]
    P=[]
    n, t = map(int, input().split())
           
    for _ in range(0, n):
        line = input()
        c, p = map(int, line.split())
        C.append(c)
        P.append(p)
   
    print(MostGold(C,P,t))


def MostGold(c,p,t):
    # initializing dpTable to -inf
    dpTable = [[float('-inf') for j in range(t + 1)] for i in range(len(c) + 1)]
    # setting the first value to 0
    dpTable[0][0] = 0
   

    # main rucursive idea 
    for i in range(len(c)):
        for j in range(1,t + 1):
            # resetting biggestVal for each new (i, j) pair
            biggestVal = float('-inf')  
            
            for k in range(i):
                biggestVal = max(biggestVal, dpTable[k][j-1])

            if(biggestVal >= c[i]) and dpTable[i][j-1] < 0:
                dpTable[i][j] = biggestVal - c[i]

            else:
                dpTable[i][j] = dpTable[i][j-1] + p[i]
   
    # Printing the Table (excluded from the Runtime Calculations)
    maxGold = max(row[-1] for row in dpTable)
    print(dpTable)
    
    return maxGold


ReadInput()