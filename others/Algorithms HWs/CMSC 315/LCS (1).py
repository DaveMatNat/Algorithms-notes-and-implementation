def LCS(A,B):
    #Create solutions array
    Solutions = [[0]*(len(B)+1) for _ in range(len(A)+1)] #2D list in python
    #Set up base cases
    #set the first row/column to 0
    #Main loop
    for i in range(1,len(A)+1):
        for j in range(1,len(B)+1):
            if (A[i-1] == B[j-1]):
                Solutions[i][j] = Solutions[i-1][j-1]+1
            else:
                Solutions[i][j] = max(Solutions[i][j-1], Solutions[i-1][j])

    
    for i in Solutions:
        print(i)

    return Solutions[len(A)][len(B)]



# print(LCS("polynomial","exponential"))
# print(LCS("crabapple","rappel"))
# print(LCS("whiteboard","habitat"))
print(LCS("jackrabbit","cricket"))
# print(LCS("GATCGACTACGCGCGATATAGGCATCGAC","CCGATAGGATAGCGCTCCGACGATCAGCAGCTACGA"))