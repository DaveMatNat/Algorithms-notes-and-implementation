def split_candy(children: int, candies: list) -> list:
    res = [0] * children
    visual = [[] for _ in range(children)]

    candies.sort()

    for i in range(children):
        popped = candies.pop()
        res[i] += popped
        visual[i].append(popped)
    
    while candies:
        min_idx = -1
        min_candies = min(res)
        for c in range(len(res)):
            if res[c] == min_candies:
                min_idx = c
                break
        popped = candies.pop()
        res[min_idx] += popped
        visual[min_idx].append(popped)
    return [i[::-1] for i in visual] # res

# print(split_candy(3, [3,4,2,2,3]))

print(split_candy(2, [3,3,3,3,4,4,4]))