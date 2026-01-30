
from collections import deque

def Bfs(G, start):
    q = deque()
    q.append(start)

    dist = [0]*(len(G))
    dist[start] = 0

    while q:
        curr = q.popleft()
        for neighbor in G[curr]:
            if neighbor not in q:
                q.append(neighbor)

                # distance of a neighbor is 0 (hasn't been assigned) or
                # the newly found distance of a neighbor is smaller than the current distance
                if dist[neighbor] == 0 or (dist[curr] + 1) <= dist[neighbor]:
                    dist[neighbor] = dist[curr] + 1


    return dist


G = {0:[1,3],
     1:[2,8],
     2:[1,7,8],
     3:[0,1,5,6,7],
     4:[2,8,9]
}


print(Bfs(G, 0))