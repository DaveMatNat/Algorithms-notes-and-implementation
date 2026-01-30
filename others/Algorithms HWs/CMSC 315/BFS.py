from collections import deque

G = [
  [1,3],
  [0,3,5,7,2],
  [1,7,6],
  [0,1,4,5],
  [3,5],
  [3,4,1,6,7],
  [5,7,2],
  [1,2,5,6]
]

G2 = [
  [1,3],
  [0,2,3,8],
  [1,7,8,4],
  [0,1,5,6,7],
  [2,8,9],
  [3,6,10],
  [3,5,7,10,11],
  [2,3,6,8,11],
  [1,2,4,7,9,11],
  [10,11,8,4],
  [5,6,11,9],
  [6,7,8,9,10]
]

def BFS(G, start):
  dist = {}
  dist[start] = 0
  q = deque()
  q.append(start)
  while(q):
    v = q.popleft() #
    for neighbor in G[v]:
      if not neighbor in dist:
        q.append(neighbor)
        dist[neighbor] = dist[v] + 1
  return dist

#print(BFS(G,0)) #Section1
# print(BFS(G2,0)) #Section2



