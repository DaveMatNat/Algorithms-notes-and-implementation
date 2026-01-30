ans = 0
P = [1,3,0,2]
n = len(P) - 1
x = 2

for i in range(n+1):
    ans += P[i] * x**i

print(ans)