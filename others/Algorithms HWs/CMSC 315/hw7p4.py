
def expMod(a, k, n):
    # Base Cases
    if (a == 0):
        return 0
    if (k == 0):
        return 1
     
    # when k is Even
    # we use the property that a^(2n) = (a^n)^2 
    halfPower = 0
    if (k % 2 == 0):
        # we recursively compute a^(k//2) mod n 
        # we reduce the exponent k by half to 
        # decrease the number of recursive calls (and so multiplications)
        halfPower = expMod(a, k//2, n)
        # we then find halfPower^2 mod n
        return (halfPower * halfPower) % n
     
    # when k is Odd
    # we use the property that a^(2n + 1) = (a^n)^2 + a
    else:

        halfPower = expMod(a, (k-1)//2, n)
        return (a * halfPower * halfPower) % n
    
 
# Testing
# a = 1234567890
# k = 1234567890
# n = 987654321  
# print(expMod(a, k, n))
print(expMod(2, 3, 3))
#385198425
