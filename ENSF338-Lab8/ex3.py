# QUESTION 2
class UnionFind:
    def __init__(self, size):
        self.parent = list(range(size))  
        self.rank = [0] * size  

    def find(self, vertex):
        if self.parent[vertex] != vertex:
            self.parent[vertex] = self.find(self.parent[vertex])  
        return self.parent[vertex]

    def union(self, vertex1, vertex2):
        root1 = self.find(vertex1)
        root2 = self.find(vertex2)
        if root1 != root2:  
            if self.rank[root1] > self.rank[root2]:
                self.parent[root2] = root1
            elif self.rank[root1] < self.rank[root2]:
                self.parent[root1] = root2
            else:
                self.parent[root2] = root1
                self.rank[root1] += 1
        return root1 != root2  

def has_cycle(graph):
    uf = UnionFind(len(graph)) 
    for u, v in graph:
        if not uf.union(u, v):  
            return True
    return False


graph = [(0, 1), (1, 2), (2, 3), (3, 4), (4, 0)]  
print(has_cycle(graph))

# QUESTION 3
class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = []  

    def add_edge(self, u, v, weight):
        self.graph.append((weight, u, v))

    def mst(self):
        self.graph.sort()  
        uf = UnionFind(self.vertices)

        mst_graph = Graph(self.vertices)  

        for edge in self.graph:
            weight, u, v = edge
            if uf.union(u, v):
                mst_graph.add_edge(u, v, weight)

        return mst_graph

    def display(self):
        for weight, u, v in self.graph:
            print(f"{u} - {v}: {weight}")

graph = Graph(5)
graph.add_edge(0, 1, 10)
graph.add_edge(0, 2, 6)
graph.add_edge(0, 3, 5)
graph.add_edge(1, 3, 15)
graph.add_edge(2, 3, 4)

mst = graph.mst()  
print("Edges in the constructed MST:")
mst.display()
