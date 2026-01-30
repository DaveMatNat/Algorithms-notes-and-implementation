def count(a, b):
    m = len(a)
    n = len(b)
 
    # Create a table to store results of sub-problems
    Solutions = [[0] * (n + 1) for i in range(m + 1)]
 
    # If first string is empty
    for i in range(n+1):
        Solutions[0][i] = 0
 
    # If second string is empty
    for i in range(m + 1):
        Solutions[i][0] = 1
 
    # Fill Solutions[][] in bottom up manner
    for i in range(1, m + 1):
        for j in range(1, n + 1):
             
            # If last characters are same,  
            # we have two options - 
            # 1. consider last characters of  
            # both strings in solution 
            # 2. ignore last character of first string 
            if a[i-1] == b[j-1]:
                Solutions[i][j] = Solutions[i-1][j-1] + Solutions[i-1][j] 
                 
            else:
                # If last character are different, ignore 
                # last character of first string 
                Solutions[i][j] = Solutions[i-1][j]

    for i in Solutions:
        print(i)
    # m: rows 
    # n: columns 
    return Solutions[m][n]


 
# Driver code 
if __name__ == '__main__':
    a = "GeeksforGeeks"
    b = "Gks"
 
    print(count(a, b))