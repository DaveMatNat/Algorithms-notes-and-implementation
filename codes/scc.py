def reverse_graph(G):
    G_reversed = {vertex: set() for vertex in G}
    
    for vertex in G:
        for neighbor in G[vertex]:
            G_reversed[neighbor].add(vertex)
    
    return G_reversed

# First DFS run
def first_dfs_setup(G):
    visited = [] # use set instead
    global clock
    global pre
    global post
    G_reverse = reverse_graph(G)

    for v in G_reverse:
        if v not in visited:
            first_dfs(G_reverse, v, visited)
    # print(f"PRE: {pre}")
    # print("---------------")
    # print(f"POST: {post}")
    return visited


def first_dfs(G, current_vertex, visited):
    visited.append(current_vertex) # use add instead
    # PRE
    global clock
    global pre
    global post
    clock += 1
    pre.append((current_vertex, clock)) # Assign pre-number

    for neighbor in G[current_vertex]:
        if neighbor not in visited:
            first_dfs(G, neighbor, visited)
    # POST
    clock += 1
    post.append((current_vertex, clock))

def cc_setup(G):
    components = {} # map: vertex -> connected_component_label
    ccnum = 1 # connected component number
    global start
    global post_copy
    post_copy = post[:]
    while post:
        highest_post = post.pop()
        # if vertex not in components.
        if highest_post[0] not in components:
            cc_recursive(G, highest_post[0], ccnum, components)
            ccnum+=1 # change label
    return components

def cc_recursive(G, current, ccnum, components):
    components[current] = ccnum
    for neighbor in G[current]:
        if neighbor not in components:
            cc_recursive(G,neighbor, ccnum, components)
        

def scc(G):
    first_dfs_setup(G)
    scc = cc_setup(G)
    return scc

clock = 0
pre = []
post = []
post_copy = []

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

print(f"SCC's")
print("\n")
print(scc(G))
print("\n")


# Run regular DFS on highest post no

def dfs_setup(G):
    visited = []
    global post_copy
    while post_copy:
        v, post_no = post_copy.pop()
        if v not in visited:
            dfs_recursive(G, visited, v)
    return visited

def dfs_recursive(G, visited, current_vertex):
    visited.append(current_vertex)
    for neighbor in G[current_vertex]:
        if neighbor not in visited:
            dfs_recursive(G, visited, neighbor)

print(f"DFS from highest post number")
print("\n")
print(dfs_setup(G))