class Graph:
    def __init__(self, graph):
        self.graph = graph
        self.reverse_graph = None

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
    

    def find_scc(self) -> tuple:
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
        
        clock = [0]
        pre = []
        post = []

        self.get_reverse_graph()
        first_dfs_setup()
        post_copy = post[:]
        scc = cc_labeling()
        traversal = path()

        return scc, traversal
        
    
if __name__ == '__main__':
    G = Graph({
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
    })

    scc, path = G.find_scc()
    print(scc)