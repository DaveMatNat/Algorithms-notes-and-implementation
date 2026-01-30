
# V1 O(n^2)
from turtle import left


def currency (B, k):
    leftover = k
    out = []
    ind = 0
    for r in range(len(B)-1, -1, -1): 
        out.append(B[r])
        out.append(0)
        while leftover >= B[r]:
            if out[ind] == B[r]:
                out[ind+1] += 1

            leftover -= B[r]

        ind += 2

    return out


# ! Make sure that key value already exists in map 
# OR add a key:value at the same time

# O(n)
def currency_v2(B, k):
    leftover = k
    out = {}

    # Iterating a set of bills in reversed order
    for r in range(len(B)-1, -1, -1):
        # Calculating the number of bills needed
        count = leftover // B[r]

        # Updating the count of each necessary bill
        if count > 0:
            out[B[r]] = count
            # Updating the leftover amount
            print(leftover, B[r])
            leftover = leftover % B[r]
            print(leftover, B[r])

    return out

print(currency_v2([1, 5, 10, 20, 50, 100], 133))
# print(currency_v2([1, 5, 10, 20, 50, 100], 0))
# print(currency_v2([1, 5, 10, 20, 50, 100], 233))
