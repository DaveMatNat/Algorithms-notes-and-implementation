from collections import defaultdict
from queue import PriorityQueue
from math import inf

#Note: Python's queue.PriorityQueue doesn't support true updates. A hack is to add
#redundant values, and ignore PriorityQueue dequeues for vertices that have
#already been processed/finalized.

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
            # print(v,curdist,neighbor,weight)
            if dist[neighbor] > curdist + weight: #O(1)
                dist[neighbor] = curdist + weight
                pq.put((dist[neighbor], neighbor)) #pq entry
    return dist

#Graph is a dictionary of dictionaries, a particularly convenient average
#case way to implement graphs in weighted situations.
#Graph[i] is a dictionary of neighbor:distance pairs from the vertex i.
#This allows the vertices to be anything - not just integers 0...n-1!
#This is the graph from the "medium sized example" from lecture on 2-1

G = {
    "A": {"B":2,"E":4, "H":8},
    "B": {"A":2,"E":3,"F":1,"C":3},
    "C": {"B":3,"F":1,"D":3},
    "D": {"C":3,"F":6,"G":3,"K":5},
    "E": {"A":4,"B":3,"F":4,"I":3,"H":2},
    "F": {"E":4,"B":1,"C":1,"D":6,"G":2,"J":7,"I":6},
    "G": {"F":2,"D":3,"K":1,"J":4},
    "H": {"A":8,"E":2,"I":2},
    "I": {"H":2,"E":3,"F":6,"J":1},
    "J": {"I":1,"F":7,"G":4,"K":2},
    "K": {"J":2,"G":1,"D":5}
    }

# print(Dijkstra(G,"A"))