





def Mining(t,c, p):
    n = len(c)
    MaxGold = [[float('-inf')] * (t+1) for _ in range(n+1)]

    MaxGold[0][0] = 0

    # for t in MaxGold:
    #     print(t)

    for i in range(len(c)):
        for j in range(1, t + 1):
            maxvalue = float('-inf')
            for k in range(i):
                maxvalue = max(maxvalue, MaxGold[k][j-1])
            if(maxvalue >= c[i]) and MaxGold[i][j-1] < 0:
                MaxGold[i][j] = maxvalue - c[i]
            else:
                MaxGold[i][j] = MaxGold[i][j-1] + p[i]
            
    
    # Printing DP table
    for t in MaxGold:
        print(t)

Mining(10,[0,1],[7,2])
