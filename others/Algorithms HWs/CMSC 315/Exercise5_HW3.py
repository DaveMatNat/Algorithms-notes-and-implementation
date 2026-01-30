from math import inf 
from collections import deque, defaultdict
from queue import PriorityQueue
from math import inf


# Author: Prateek Bhakta
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


# Author: Prateek Bhakta
def Dijkstra(G,start):
    dist = defaultdict(lambda: inf) #dist to all vertices defaults to inf
    finished= set() #Hack because python'inpChargers PriorityQueue isn't updateable
    pq = PriorityQueue()
    for v in G: pq.put((inf,v)) #Adding elements into a pq
    pq.get((inf,start))
    pq.put((0,start))
    dist[start] = 0
    while(not pq.empty()): #loop over all vertices once
        curdist,v = pq.get() #PQ pop()
        if v in finished: continue #hack because pythonPriorityQueue isn't great
        finished.add(v)
        for neighbor,weight in G[v].items(): #Iteration over all neighbors of v
            # print(v,curdist,neighbor,weight)
            if dist[neighbor] > curdist + weight: #O(1)
                dist[neighbor] = curdist + weight
                pq.put((dist[neighbor], neighbor)) #pq entry
    return dist

# Function that builds initial graph G
def BuildGraph():

    n, m, c, k = map(int,input().split())
    vertexList = list(map(int,input().split()))

    
    G = []
    for i in range(0, n - 1):
        G.append(list(map(int, input().split())))
    G.append([])

    end = n-1

    vertexList.append(end)

    return n, k, G, vertexList


def ShortestPossiblePath(): 
    n, k, G, vertexList = BuildGraph()

    # Building new graph G'
    Gprime = {} 
    for v1 in vertexList: 
        # Running BFS 
        dict = BFS(G, v1) 
        for v2 in vertexList: 
            if v2 in dict: 
                if dict[v2] <= k: 
                    temp = {} 
                    if v1 in Gprime: 
                        temp = Gprime[v1] 
                        temp[v2] = dict[v2]
                    else: 
                        temp = {v2: dict[v2]} 
                    Gprime[v1] = temp 

    out = Dijkstra(Gprime, 0) 

    if (out[n-1] == inf): 
        return "Impossible" 
    else: 
        return out[n-1] 

print(ShortestPossiblePath()) 
   
