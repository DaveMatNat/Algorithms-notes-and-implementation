
# def MIS(A, n):
#     #Set up the array to store the subproblems
#     S = [0]*(len(A)+1)
#     #Set up base cases
#     S[0] = 0
#     S[1] = max(0,A[0])
#     #Main recursive loop
#     for i in range(2,len(A)+1):
#         S[i] = max(S[i-n],A[i-n] + S[i-(n+1)])
#     #Return the answer
#     return S
def MIS_k(A, k):
    #Set up the array to store the subproblems
    S = [0] * (len(A)+1)
    #Set up base cases
    S[0] = 0
    S[1] = max(0, A[0])
    #Main recursive loop
    for i in range(2, len(A)+1):
        S[i] = max(A[i-1] + S[max(0, i-1-k)], S[i-1])
    #Return the answer
    return S

# Example usage
print(MIS_k([9,1,1,1,8,1,9,1,1,1,9], 2))


# a = [4, 2, 9, 8, 3, 6, 2, 3, 1, 2, 5]
# b = [9,1,1,1,8,1,9,1,1,1,9]
# res = MIS(b, 2)
# print(res)
# print(max(res))
