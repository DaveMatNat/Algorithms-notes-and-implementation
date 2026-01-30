G = {
    1: {2},
    2: {1,3},
    3: {2},
    4: {5},
    5: {4}
}

def dfs_setup(G, start):
    visited = [] # use set instead
    dfs_recursive(G, start, visited)
    return visited


def dfs_recursive(G, current_vertex, visited):
    visited.append(current_vertex) # use add instead
    for neighbor in G[current_vertex]:
        if neighbor not in visited:
            dfs_recursive(G, neighbor, visited)
        

print(f"DFS at A")
print(dfs_setup(G, 1))
print(f"\nDFS at B")
print(dfs_setup(G, 2))
print(f"\nDFS at C")
print(dfs_setup(G, 3))
print(f"\nDFS at D")
print(dfs_setup(G, 4))
print(f"\nDFS at E")
print(dfs_setup(G, 5))
