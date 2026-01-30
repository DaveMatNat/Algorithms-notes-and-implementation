# def most_gold(t, c, p):
#     n = len(c)  # Number of available pickaxes
#     dp = [[float('-inf')] * (t+1) for _ in range(n+1)]
    
#     # Base case: At time 0, you have 0 gold
#     for i in range(n+1):
#         dp[i][0] = 0
    
#     for i in range(1, n+1):
#         for j in range(1, t+1):
#             for k in range(j+1):
#                 if k <= len(dp[i-1]):
#                     dp[i][j] = max(dp[i][j], dp[i-1][k] + (j-k) * p[i-1] - c[i-1])
    
#     return dp

# # Example usage:
# t = 3
# c = [1]  # Costs of pickaxes
# p = [2]  # Productivities of pickaxes

# print(most_gold(t, c, p))  # Output: 7

# def Mining(t,c, p):
#     n = len(c)
#     MaxGold = [[float('-inf')] * (n) for _ in range(t+1)]

#     for i in range(n+1):
#         MaxGold[i][0] = 0

#     # for t in range(0, t+1):
#     #     print(t)
        
#         # MaxGold[t][0] = t
#         biggestPick = MaxGold[t][0]
#         for j in range(0, n):

#             # checking if we can afford the new pickaxe
#             if biggestPick >= c[j]:
#                 print("Keep the pick: ", MaxGold[t-1][j] + p[j])
#                 print("Just bought new: ", MaxGold[t-1][j-1] - c[j])
#                 print("Biggest is: ", max(MaxGold[t-1][j] + p[j], MaxGold[t-1][j-1] - c[j]))
#                 MaxGold[t][j] = max(MaxGold[t-1][j] + p[j], MaxGold[t-1][j-1] - c[j])
#                 if MaxGold[t][j] > biggestPick:
#                     biggestPick = MaxGold[t][j]

#             else:
#                 print("can't afford")
#                 MaxGold[t][j] = MaxGold[t-1][j] + p[j]
#                 if MaxGold[t][j] > biggestPick:
#                     biggestPick = MaxGold[t][j]

#         print(MaxGold[t])

#         print("Pick Greatest Value: ", biggestPick)

#     print()
#     # Printing DP table
#     for t in MaxGold:
#         print(t)
            
# Mining(7,[2,4],[2,3])
# # Mining(7,[1,2,4],[1,2,3])


# def Mining(t,c, p):
#     n = len(c)
#     MaxGold = [[float('-inf')] * (t+1) for _ in range(n+1)]

#     for i in range(n+1):
#         MaxGold[i][0] = 0

#     for i in range(len(c)):
#         for j in range(1, t + 1):
#             maxvalue = float('-inf')
#             for k in range(i):
#                 maxvalue = max(maxvalue, MaxGold[k][j-1])
#             if(maxvalue >= c[i]) and MaxGold[i][j-1] < 0:
#                 MaxGold[i][j] = maxvalue - c[i]
#             else:
#                 MaxGold[i][j] = MaxGold[i][j-1] + p[i]
            
    
#     # Printing DP table
#     for t in MaxGold:
#         print(t)


def main():
    #inputs
    C=[]
    P=[]
    n, t = map(int, input().split())
           
    for num in range(0, n):
        line = input()
        c, p = map(int, line.split())
        C.append(c)
        P.append(p)
#    C=[0,2,4,8,10]
#    P = [1,2,3,4,5]
#    t = 10
    # print(C,P)
   
    print(MostGold(C,P,t))
   
def MostGold(c,p,t):
    #initialize table to -inf
    table = [[float('-inf') for j in range(t + 1)] for i in range(len(c) + 1)]
    #initialize first value to 0
    table[0][0] = 0
   
    #  # Printing DP table
    # for t in table:
    #     print(t)

    #update table
    for i in range(len(c)):
        for j in range(1,t + 1):
            maxvalue = float('-inf')  # Reset maxvalue for each new (i, j) pair
            for k in range(i):
                maxvalue = max(maxvalue, table[k][j-1])
            if(maxvalue >= c[i]) and table[i][j-1] < 0:
                table[i][j] = maxvalue - c[i]
            else:
                table[i][j] = table[i][j-1] + p[i]
   
    maxGold = max(row[-1] for row in table)
    print(table)
    return maxGold

main()

