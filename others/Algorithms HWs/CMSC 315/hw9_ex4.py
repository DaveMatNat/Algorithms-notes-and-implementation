def MaxPoints(points, h):
    n = len(points)
    dpTable = [[0] * (h + 1) for _ in range(n + 1)]
    choices = [[0] * (h + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, h + 1):
            dpTable[i][j] = dpTable[i - 1][j]
            choices[i][j] = 0
            for k in range(j + 1):
                if dpTable[i][j] < dpTable[i - 1][j - k] + points[i - 1][k]:
                    dpTable[i][j] = dpTable[i - 1][j - k] + points[i - 1][k]
                    choices[i][j] = k

    total_points = dpTable[n][h]
    time_allocation = [0] * n
    i, j = n, h
    while i > 0:
        time_allocation[i - 1] = choices[i][j]
        j -= choices[i][j]
        i -= 1

    return total_points, time_allocation

# points1 = [[0, 50, 75, 90, 100, 100, 100],
#            [0, 80, 100, 100, 100, 100, 100],
#            [0, 40, 70, 80, 90, 95, 100]]
# h1 = 6
# print(MaxPoints(points1, h1))  


