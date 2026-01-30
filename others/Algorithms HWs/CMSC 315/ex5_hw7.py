
def hill(A):
    # If array has only one element
    if len(A) == 1: 
        return A[0]
    
    # Checking if the first element is a hill
    if A[0] >= A[1]:
        return A[0]
    
    # pointers to track previous and next item in array
    prv = 0
    nxt = 2
    for curr in range(1, len(A)-1):
        # finding the hill
        if A[prv] <= A[curr] and A[nxt] <= A[curr]:
            return A[curr]
        else:
            prv += 1
            nxt += 1

    # If there is no hill found at the end of the for loop
    # then the last element must be a hill
    return A[len(A)-1]

# print(hill([5]))
# print(hill([5,4,3,2,1]))
# print(hill([1,2,3,4,5]))
# print(hill([1,2,5,2,1]))
# print(hill([1,2,5,2,1,4,6,7,2,1,3]))


def hillRecursion(A, left, right):

    # If array has only one element
    if len(A) == 1: 
        return A[0]
    
    # Checking if the first element is a hill
    if A[left] >= A[left+1]:
        return A[left]
    
     # Checking if the last element is a hill
    if A[right] >= A[right-1]:
        return A[right]
    
    mid = (left + right) // 2
   
    # middle is the hill
    if A[mid-1] <= A[mid] and A[mid] >= A[mid+1]:
        return A[mid]
    
    # middle is on the upward slope
    elif A[mid-1] <= A[mid] and A[mid] <= A[mid+1]:
        return hillRecursion(A, mid+1, right)
    
    # middle is on the downward slope
    else:
        return hillRecursion(A, left, mid)
    

a1 = [5,4,3,2,1]
a2 = [1,2,3,4,5]
a3 = [1,2,5,2,1]
a4 = [1,2,5,2,1,4,6,7,3,2,1]
a5 = [5]

# print(hillRecursion(a1, 0, len(a1)-1))
# print(hillRecursion(a2, 0, len(a2)-1))
# print(hillRecursion(a3, 0, len(a3)-1))
# print(hillRecursion(a4, 0, len(a4)-1))
# print(hillRecursion(a5, 0, len(a5)-1))
    



def kHillRecursion(A, left, right, k):
    if k == 1:
        hillRecursion(A, left, right)
 
    if left == right:
        return A[left]
    
    mid = (left + right) // 2

    # checking if middle element is a hill
    if hillChecking(A, mid, k):
        return A[mid]
    
    # UPDATED to look at mid - k
    if A[mid-k] > A[mid+k]:
        return kHillRecursion(A, left, mid-1, k)
    else:
        return kHillRecursion(A, mid+1, right, k)

# Support function
def hillChecking(A, x, k):
    for i in range(1, k+1):
        if (A[max(0, x-i)] > A[x] and x-i >= 0 
            or A[min(len(A)-1, x+i)] > A[x] and x+i < len(A)):
            return False
    return True 

# a6 = [1, 3, 5, 4, 2, 6, 7, 9, 8]
a10 = [1,2,3,4,5,4,6,7,8,7,6]
a11 = [7,6,5,4,5,4,5]
a12 = [1,2,3,4,5,4,3,2,1,1,1,1]
a13 = [1,2,3,2,1]
a14 = [1,2,3,4,5,6,7,6]

# print(kHillRecursion(a6, 0, len(a5)-1, 2))
print(kHillRecursion(a10, 0, (len(a10)-1), 2))
print(kHillRecursion(a11, 0, (len(a11)-1), 2))
print(kHillRecursion(a12, 0, (len(a12)-1), 3))
print(kHillRecursion(a13, 0, (len(a13)-1), 1))
print(kHillRecursion(a14, 0, (len(a14)-1), 2))






