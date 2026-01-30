from math import inf
from collections import defaultdict
from queue import PriorityQueue
from collections import deque

def Dijkstra(G,start):
    dist = defaultdict(lambda: inf) #dist to all vertices defaults to inf
    finished= set() #Hack because python's PriorityQueue isn't updateable
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
            if dist[neighbor] > curdist + weight: #O(1)
                dist[neighbor] = curdist + weight
                pq.put((dist[neighbor], neighbor)) #pq entry
    return dist


def edmondsKarp(fg, s, t):
    maxflow = 0
    while(True):
        minpath = defaultdict(lambda:(inf,None)) #"visited" and "parent"
        queue=deque()
        queue.append(s)
        while queue:
            u = queue.popleft()
            for v,w in fg[u].items():
                if minpath[v][1] == None and w > 0:
                    queue.append(v)
                    minpath[v] = min(minpath[u][0],w),u
        newflow = minpath[t][0]
        if minpath[t][1]==None: return maxflow
        elif minpath[t][0] == inf: return inf
        cur = t
        while(cur != s and cur != None):
            pre = minpath[cur][1]
            fg[pre][cur] -= newflow
            fg[cur][pre] += newflow
            cur = pre
        maxflow += newflow


n,m,c = map(int,input().split())

spots = list(map(int,input().split()))

roads = defaultdict(dict)
for i in range(m):
    xi,yi,d = map(int, input().split())
    if xi not in roads[yi]:
        roads[yi][xi] = d
    if yi not in roads[xi]:
        roads[xi][yi] = d

cars = {}
for i in range(c):
    vertex, miles = map(int, input().split())
    cars[i] = {vertex:miles}


nfg = defaultdict(lambda: defaultdict(int))    
nfg['s'] = {}

for car in range(c):
    nfg['s'][car] = 1

for car_v, car_m in cars.items():
    start = list(car_m.keys())[0]
    mileage = list(car_m.values())[0]

    #Find shortest paths to all other vertices using Dijkstra's algorithm
    dist = Dijkstra(roads,start)
    reachable = {}
    for v,d in dist.items():
        if d <= mileage and spots[v] != 0:
            nfg[car_v][-v] = 1
       
for x in range(1, n):
    nfg[-x]['t'] = spots[x]

#Run Edmonds Karp
maxFlow = edmondsKarp(nfg, 's', 't')
print(maxFlow)
