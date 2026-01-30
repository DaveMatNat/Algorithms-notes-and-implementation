

# def sumOfInts(w):
#     sumw = [0]*len(w)

#     for i in range(len(w)):
#         sumw[i] = sumw[i-1] + w[i]

#     return sumw

# w = [1,1,2,1,3]
# # w = [1,1,1,1,1,1,1,1,1]
# print(sumOfInts(w))
# Part 1: Computing the running sum array in O(n) time
def sumOfInts(w):
    sumw = [0]*len(w)
    sumw[0] = w[0]

    for i in range(1, len(w)):
        sumw[i] = sumw[i-1] + w[i]

    return sumw

# Part 2: Random sampling algorithm in O(log n) time
import random

def weightedRandomSample(w):
    n = len(w)
    sumw = sumOfInts(w)

    # Generate a random real number in the range [0,1)
    target = random.random() * sumw[-1]

    # Binary search to find the index where target falls in the sumw array
    low, high = 0, n-1
    while low < high:
        mid = (low + high) // 2
        if target > sumw[mid]:
            low = mid + 1
        else:
            high = mid

    return low

# Testing the weighted random sampling algorithm
w = [1, 1, 2, 1, 3]
samples = [0] * len(w)
total_samples = 10000

for _ in range(total_samples):
    index = weightedRandomSample(w)
    samples[index] += 1

# Print the normalized frequencies of each index
for i, freq in enumerate(samples):
    print(f"Index {i}: {freq/total_samples}")
