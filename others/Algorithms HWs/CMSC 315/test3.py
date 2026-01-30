def MinWeightIn2dArray(A, n, m):
    # Initialize the 2D array with infinity
    S = [[float('inf') for _ in range(n)] for _ in range(m)] 

    if len(A) == 0:
        return 0
    
    # Set the starting point to its value
    S[0][0] = A[0][0]
    
    # Fill the first row and first column
    for i in range(1, m):
        S[i][0] = S[i-1][0] + A[i][0]
    for j in range(1, n):
        S[0][j] = S[0][j-1] + A[0][j]



    # Fill the rest of the array
    for i in range(1, m):
        for j in range(1, n):
            S[i][j] = min(S[i-1][j], S[i][j-1]) + A[i][j]

    # Uncomment this to print the array
    for row in S:
        print(row)

    return S[m-1][n-1]

A = [
    [3, 4, 1, 10, 2, 1, 4],
    [7, 2, 11, 7, 3, -1, 2],
    [3, 1, 12, -3, 14, 1, 5],
    [2, 1, 3, 2, 3, 4, 1],
    [4, 6, 2, 4, 10, -1, 3]
]

n = 7
m = 5

print(MinWeightIn2dArray(A, n, m))  # Output should be 28
