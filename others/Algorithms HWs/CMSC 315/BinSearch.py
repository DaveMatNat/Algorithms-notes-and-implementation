
from tkinter import NO


def BinSearch(A, target, left=0, right=None, count=0):
    if right is None : right = len(A)

    # Base case
    if left + 1 == right:
        if A[left] == target:
            return left, count
        else:
            return None
        
    
    mid = (left + right)//2
    if A[mid] <= target:
        return BinSearch(A, target, mid, right, count+1)
    else:
        return BinSearch(A,target, left, mid, count+1)

A = [3,4,8,10,10,14,15,19,19,19,19,24,30,32]

print(BinSearch(A, 12))
print(BinSearch(A, 14))