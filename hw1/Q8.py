def WonkySum(A,B):
    s = 0
    res = ""
    for i in range(len(A)):
        curr = 0
        for j in range(B[i]):
            curr += A[j]
            s += A[j]
        res += f"{curr}" if i == len(A)-1 else f"{curr} + "
    print(res)
    return s

A = [3,7,-2,9]
B = [0,3,4,4]
print(WonkySum(A,B))