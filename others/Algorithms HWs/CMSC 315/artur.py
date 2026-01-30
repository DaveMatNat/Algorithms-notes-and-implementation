ans = 0
n = 4
P = [2,-6,2,-1]
x = 3


n = len(P) - 1
ans = P[n]



for i in range(n-1,-1,-1):
    ans = ans * x + P[i]

print(ans)