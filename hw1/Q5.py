def build_prefix_sum(arr):
    prefix_sum = [0] * len(arr)
    prefix_sum[0] = arr[0]
    
    for k in range(1, len(arr)):
        prefix_sum[k] = arr[k] + prefix_sum[k-1]
    
    return prefix_sum


def range_sum(prefix_sum, i, j):
    if i == 0:
        return prefix_sum[j]
    else:
        return prefix_sum[j] - prefix_sum[i-1]
    

prefix_arr = build_prefix_sum([4,5,7,8,9])

print(range_sum(prefix_arr,1,3))