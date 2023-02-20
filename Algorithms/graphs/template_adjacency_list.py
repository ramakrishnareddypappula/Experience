
# sample adjacency list code:

class Graph():
    def __init__(self, vertices_size):
        self.vertices_size = vertices_size
        self.adj_list = [[0 for _ in range(self.vertices_size)] for _ in range(self.vertices_size)]

    def addEdge(self, start, end, is_undirected=True):
        self.adj_list[start].append(end)
        if is_undirected:
            self.adj_list[end].append(start)

    def has_euler_cycle(self):
        for vertex in self.adj_list:
            if len(vertex) % 2 == 1:
                return False
        return True

    def has_euler_path(self):
        count = 0
        for vertex in self.adj_list:
            if len(vertex) % 2 == 1:
                count += 1
        if count == 0 or count == 2:
            return True
        return False


g = Graph(10)
g.addEdge(0, 6)
g.addEdge(0, 1)
g.addEdge(4,3)


