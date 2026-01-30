

def MinWeightIn2dArray(A, n, m):
    S= list([[1 for i in range(n)] for i in range(m)]) 
    # S = [[float('inf') for _ in range(n)] for _ in range(m)] 

    # Base Case
    if len(A) == 0:
        return 0
    
    # Set the starting point to its value
    S[0][0] = A[0][0]

    # Fill the first row and first column
    for i in range(1, m):
        S[i][0] = S[i-1][0] + A[i][0]
    for j in range(1, n):
        S[0][j] = S[0][j-1] + A[0][j]
    
    for i in range(1, m):
        for j in range(1, n):
            S[i][j] = min(S[i-1][j] + A[i][j], S[i][j-1] + A[i][j])

    for row in S:
        print(row)

    return S[i][j]

A= [[3,4,1,10,2,1,4],
    [7,2,11,7,3,-1,2],
    [3,1,12,-3,14,1,5],
    [2,1,3,2,3,4,1],
    [4,6,2,4,10,-1,3]
]

print(MinWeightIn2dArray(A,7,5))