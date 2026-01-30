class Graph:
    def __init__(self, graph):
        self.G = graph
        self.reverse = None

    def get_reverse_graph(self):
        if self.reverse is None:
            G_reversed = {vertex: set() for vertex in self.G}
            for vertex in self.G:
                for neighbor in self.G[vertex]:
                    G_reversed[neighbor].add(vertex)
            self.reverse = G_reversed
        return self.reverse
    

    def find_scc(G) -> (list, list):
        """
        :param G: G is a graph with key as the vertex and value of hashmap of directed neighbors.
        :return: List of grouped SCC, and 
        :rtype: list
        """
    