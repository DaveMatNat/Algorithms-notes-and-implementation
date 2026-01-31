from collections import deque

class Graph:
    def __init__(self, graph, is_directed=False):
        self.graph = graph
        self.reverse_graph = None
        self.is_directed = is_directed

    def get_reverse_graph(self):
        """
        Returns the reverse of the graph (arrows point the other way around)
        """
        if not self.reverse_graph:
            self.reverse_graph = {vertex: set() for vertex in self.graph}
            for vertex in self.graph:
                for neighbor in self.graph[vertex]:
                    self.reverse_graph[neighbor].add(vertex)
        return self.reverse_graph
    
    def dfs_path(self, start, print_depth=False):
        visited = []
        if print_depth:
            print("\t DFS Depth \n")
            print(start)

        def dfs_recursive(current_vertex, depth=1):
            visited.append(current_vertex)
            for neighbor in self.graph[current_vertex]:
                if neighbor not in visited:
                    if print_depth:
                        print(f"{"\t" * depth}{neighbor}")
                        dfs_recursive(neighbor, depth + 1)
                    else:
                        dfs_recursive(neighbor)
        
        dfs_recursive(start)
        return visited
    
    def bfs_path(self, start):
        """
        :param start: Starting vertex to start BFS search

        Return: 
            tulple of order visited, and distances hashmap ( vertex -> distance from start)
        """

        visited = []
        distances = {}
        distance = 1

        queue = deque()
        queue.append(start)
        distances[start] = 1

        while queue:
            current_vertex = queue.popleft()
            visited.append(current_vertex)
            for neighbor in self.graph[current_vertex]:
                if neighbor not in distances:
                    distances[neighbor] = distances[current_vertex] + 1
                    queue.append(neighbor)

        return visited, distances

    def find_scc(self, print_scc = False) -> tuple:
        """
        :param G: G is a graph with key as the vertex and value of hashmap of directed neighbors.
        :return: (List of grouped SCC, Traversal order from highest post no.)
        :rtype: tuple
        """

        def first_dfs_setup():
            """
            Runs dfs of the reverse graph, populating pre and post with tuples (VERTEX, pre/post #)
            """

            def first_dfs(current_vertex, visited):
                """
                DFS helper for first_dfs_setup()
                """

                visited.append(current_vertex)

                # PRE
                clock[0] += 1
                pre.append((current_vertex, clock[0])) # Assign pre-number

                for neighbor in self.reverse_graph[current_vertex]:
                    if neighbor not in visited:
                        first_dfs(neighbor, visited)

                # POST
                clock[0] += 1
                post.append((current_vertex, clock[0]))

            visited = []

            for vertex in self.reverse_graph:
                if vertex not in visited:
                    first_dfs(vertex, visited)
        
        def cc_labeling():
            """
            Connected Components Labeling
            """
            
            def cc_recursive(current, component_label):
                """
                :param current: current vertex
                :param ccnum: connected component number label
                """
                components[current] = component_label
                for neighbor in self.graph[current]:
                    if neighbor not in components:
                        cc_recursive(neighbor, component_label)
            
            components = {} # map: vertex -> connected_component_label
            component_label = [1] # connected component number

            while post:
                highest_post = post.pop()
                # if vertex not in components.
                if highest_post[0] not in components:
                    cc_recursive(highest_post[0], component_label[0])
                    component_label[0] += 1 # increment label

            return components

        def path():
            """
            Returns a list of DFS path according to Highest Post Number
            """
            def dfs_recursive(current_vertex):
                visited.append(current_vertex)
                for neighbor in self.graph[current_vertex]:
                    if neighbor not in visited:
                        dfs_recursive(neighbor)

            visited = []

            while post_copy:
                vertex, post_num = post_copy.pop()
                if vertex not in visited:
                    dfs_recursive(vertex)
            return visited
        
        def print_pretty_scc():
            """
            
            :param self: Description
            :param scc: Strongly connected component (Connected_component_label -> list of vertices)
            """
            ls = { i: list() for i in range(min(scc.values()), max(scc.values())+1) }
            for k,v in scc.items():
                ls[v].append(k)
            
            print(f"\n\tStrongly Connected Components \n")
            for cc in ls.values():
                print(*cc, sep=" ")
            print()
        
        if not self.is_directed:
            print(f"Graph is NOT directed, cannot find SCC")
            return None
        
        clock = [0]
        pre = []
        post = []

        self.get_reverse_graph()
        first_dfs_setup()
        post_copy = post[:]
        scc = cc_labeling()
        traversal = path()

        if print_scc:
            print_pretty_scc()

        return scc, traversal
    
if __name__ == '__main__':
    # G1 = Graph({
    #     'A':{'B','F'},
    #     'B':{'E','G'},
    #     'C':{'B','D','F'},
    #     'D':{'H'},
    #     'E':{'A','I'},
    #     'F':{'I'},
    #     'G':{'F','H','J','K'},
    #     'H':{'L'},
    #     'I':{'F'},
    #     'J':{'E','I','K'},
    #     'K':{'H'},
    #     'L':{'K'}
    # }, True)

    # scc, path = G1.find_scc(print_scc=True)

    # G1.dfs_path('A',print_depth=False)
    # print(G1.bfs_path('A')[0])

    Valid = Graph({
        'Z':{'A','_D'},
        'A':{'B'},
        'B':{'C', '_D'},
        'C':{},
        'D':{'_Z', '_B'},
        '_Z':{'Z'},
        '_A':{'_Z'},
        '_B':{'_A'},
        '_C':{'_B'},
        '_D':{},
    }, True)

    # scc, path = Valid.find_scc(print_scc=True)

    Invalid = Graph({
        'Z':{'A','_D'},
        'A':{'B', '_C'},
        'B':{'C', '_D'},
        'C':{'_A'},
        'D':{'_Z', '_B'},
        '_Z':{'Z'},
        '_A':{'_Z'},
        '_B':{'_A'},
        '_C':{'_B'},
        '_D':{},
    }, True)

    scc, path = Invalid.find_scc(print_scc=True)
    print(path)