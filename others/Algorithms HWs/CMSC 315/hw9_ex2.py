def CardGame(cards):
    n = len(cards)
    dpTable = [[0] * n for _ in range(n)]
   
    for length in range(1, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            if length == 1:
                dpTable[i][j] = cards[i]
            elif length == 2:
                dpTable[i][j] = max(cards[i], cards[j])
            else:
                dpTable[i][j] = max(
                    cards[i] + min(dpTable[i + 2][j], dpTable[i + 1][j - 1]),
                    cards[j] + min(dpTable[i + 1][j - 1], dpTable[i][j - 2])
                )
   
    return dpTable[0][n - 1]

# cards1 = [3, 3, 3, 2, 6, 2, 5, 8]
# print(CardGame(cards1))  

