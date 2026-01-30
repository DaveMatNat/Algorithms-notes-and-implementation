def eval_1(A,x):
    sum = 0
    temp_x = 1
    for i in range(len(A)):
        sum += A[i] * temp_x
        temp_x *= x
    return sum

def eval_2(A,x):
    sum = 0
    for i in range(len(A)):
        temp = A[i]
        for j in range(i):
            temp *= x
        sum += temp
    return sum

def eval_3(A,x):
    sum = 0
    for i in range(len(A)):
        temp = A[i]
        for j in range(i):
            temp *= x
            for k in range(len(A)):
                temp *= 1
        sum += temp
    return sum

import time
import random

n = 500  # Desired list size
min_val = 1
max_val = 100

random_list = [random.randint(min_val, max_val) for _ in range(n)]



start = time.time()
eval_1(random_list,n)
end = time.time()
time_1 = end - start

start = time.time()
eval_2(random_list,n)
end = time.time()
time_2 = end - start

start = time.time()
eval_3(random_list,n)
end = time.time()
time_3 = end - start

print(f"Time for eval_1: {time_1}")
print(f"Time for eval_2: {time_2}")
print(f"Time for eval_3: {time_3}")
print(f"Ratio 2 / 1: {time_2 / time_1}")
print(f"Ratio 3 / 1: {time_3 / time_1}")