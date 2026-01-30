N = 100
for i in range(1,N):
    for j in range(1,N):
        if (j**2 % i == 0):
            if (j % i != 0):
                print(i,j)