import time
import random

def Intersection_Hash(A,B):
    intersection = []
    hashset_b = set(B)
    for a in A:
        if a in hashset_b:
            intersection.append(a)
    return intersection

def bin_search(arr, target):
    l = 0
    r = len(arr) - 1
    while l <= r:
        mid = (l+r)//2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            l = mid + 1
        else:
            r = mid - 1
    return -1

def Intersection_Bin(A, B):
    intersection = []
    B.sort()

    for x in A:
        # binary search
        idx = bin_search(B, x)
        if idx != -1:
            intersection.append(B[idx])
    return intersection

def Intersection_Nested(A, B):
    intersection = []
    for x in A:
        for y in B:
            if x == y:
                intersection.append(x)
                break #No need to continue this loop
    return intersection


A = random.sample(range(1000000), 500000)
B = random.sample(range(1000000), 2000)

print(f"A size: {len(A)}, B size: {len(B)}")

# Time Hash Set Method
start = time.perf_counter()
algo_hash = Intersection_Hash(A, B)
end = time.perf_counter()
print(f"Hash Set Intersection Time:      {end - start:.8f} seconds")

# Time Binary Search Method
start = time.perf_counter()
algo_bin = Intersection_Bin(A[:], B[:]) # Slicing to pass copies
end = time.perf_counter()
print(f"Binary Search Intersection Time: {end - start:.8f} seconds")

# Time Nested Loop Method
# Warning: This takes a long time (O(N*M) = 10^9 operations)
print("Starting Nested Loop...")
start = time.perf_counter()
algo_nested = Intersection_Nested(A, B) 
end = time.perf_counter()
print(f"Nested Loop Intersection Time:   {end - start:.8f} seconds")

print("-" * 30)
print(f"Hash Set res: {len(algo_hash)}")
print(f"Binary Search res: {len(algo_bin)}")
print(f"Nested Loop res: {len(algo_nested)}")
