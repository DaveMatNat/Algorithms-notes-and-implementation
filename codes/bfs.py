# BFS

from collections import deque

def bfs(G, s):
    distances = {}
    distances[s] = 0
    q = deque()
    q.append(s)

    while q:
        current_node = q.popleft()
        print(current_node)
        for neighbor in G[current_node]:
            if neighbor not in distances:
                distances[neighbor] = distances[current_node] + 1
                q.append(neighbor)
    return distances

G = {
    4: {6,2},
    6: {5},
    2: {3,1},
    3: {},
    5: {},
    1: {}
}

print(bfs(G, 4))