
def SubSum(A, t):
    Solutions = list([[False for i in range(t + 1)] for i in range(len(A) + 1)]) 

    # Base Cases:
    for i in range(len(A)+1):
        Solutions[i][0] = True

    for j in range(1,t+1):
        Solutions[0][j] = False
    
    for i in range(1,len(A)+1):
        for j in range(1,t+1):
            if j < A[i-1]:
                Solutions[i][j] = Solutions[i-1][j]
            else:
                Solutions[i][j] = Solutions[i-1][j] or Solutions[i-1][j-A[i-1]]


    # printing table
    # for i in Solutions:
    #     print(i)

    return Solutions[len(A)][t]


print(SubSum([5,2,23,13,30,18],20))
print(SubSum([1,2,3,4,5],1))
print(SubSum([2,2,3,4,5],1))
print(SubSum([3,5,9,15,30,40],55))
print(SubSum([3,5,9,15,30,40],61))

