def cc_setup(G):
    components = {} # map: vertex -> connected_component_label
    ccnum = 1 # connected component number
    for v in G:
        if v not in components:
            cc_recursive(G, v, ccnum, components)
            ccnum+=1 # change label
    return components

def cc_recursive(G, current, ccnum, components):
    components[current] = ccnum
    for neighbor in G[current]:
        if neighbor not in components:
            cc_recursive(G,neighbor, ccnum, components)

