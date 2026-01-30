

def eclipse_happiness(happiness, c):
    Solutions = list([[0 for i in range(len(c) + 1)] for i in range(len(c) + 1)]) 

    # n = len(h)
    # m = len(clouds)

    # Initialize DP table with maximum possible value
    # dp = [[float('inf')] * (m + 1) for _ in range(n + 1)]
    # dp[0][0] = 0  # Base case: No seconds and no clouds
    for j in range(1,len(c)+1):
        Solutions[0][j] = 0


    for i in range(1,len(happiness)+1):
        for j in range(1,len(c)+1):
            if i - c[j-1] < 0:
                Solutions[i][j] = Solutions[i-1][j] + happiness[i-1]
            else:
                Solutions[i][j] = min(Solutions[i-c[j-1]][j-1], Solutions[i-1][j] + happiness[i-1])

    # for i in range(1, n + 1):
    #     for j in range(1, m + 1):
    #         # Case 1: Block current second with cloud j
    #         if i >= clouds[j - 1]:
    #             dp[i][j] = min(dp[i][j], dp[i - clouds[j - 1]][j - 1])

    #         # Case 2: Don't block current second
    #         dp[i][j] = min(dp[i][j], dp[i - 1][j] + h[i - 1])

    # printing table
    for happiness in Solutions:
        print(i)

    # return dp[n][m]


# Test case
happiness_values = [2, 3, 4, 8]
cloud_lengths = [1, 2]
result = eclipse_happiness(happiness_values, cloud_lengths)
# print("Minimum possible happiness:", result)  # Output: 18

# happiness = [2, 3, 4, 8, 7, 6, 4]
# clouds = [3, 1, 2]
# result = eclipse_happiness(happiness, clouds)
# print("Minimum possible happiness:", result)