G = {
    'A':{'B','F'},
    'B':{'E','G'},
    'C':{'B','D','F'},
    'D':{'H'},
    'E':{'A','I'},
    'F':{'I'},
    'G':{'F','H','J','K'},
    'H':{'L'},
    'I':{'F'},
    'J':{'E','I','K'},
    'K':{'H'},
    'L':{'K'}
}

# G = {
#     1: {2},
#     2: {1,3,4},
#     3: {2,5},
#     4: {5},
#     5: {2}
# }

def dfs_setup(G, start):
    visited = []
    depth = 0
    dfs_recursive(start, visited, G, depth)
    return visited


def dfs_recursive(current_vertex, visited, G, depth):
    visited.append(current_vertex)
    space = "\t"*depth
    print(f"{space}{current_vertex}")
    for neighbour in G[current_vertex]:
        if neighbour not in visited:
            dfs_recursive(neighbour, visited, G, depth + 1)

# for i in G:
#     print(dfs_setup(G, i))
#     print()

dfs = dfs_setup(G, 'A')

print()

print(dfs)