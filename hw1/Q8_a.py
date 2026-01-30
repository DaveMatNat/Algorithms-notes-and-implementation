def WonkySum(A,B):
    total_sum = 0
    prev_sum = 0
    prev_b = 0

    # for each b in B (where b means from 0 ... b - 1)
    for b in B:
        for index in range(prev_b, b): # (this goes from prev_b ... b - 1)
            prev_sum += A[index] # prev_sum = A[prev_b] + ... + A[b - 1]
        total_sum += prev_sum
        prev_b = b

    return total_sum

A = [3,7,-2,9]
B = [0,3,4,4]
print(WonkySum(A,B))