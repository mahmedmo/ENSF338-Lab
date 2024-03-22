import timeit

class GraphNode:
    def __init__(self, data):
        self.data = data
        self.edges = {}
        self.visited = False

class Graph1:
    def __init__(self):
        self.nodes = {}
        
    def addNode(self, data):
        node = GraphNode(data)
        self.nodes[data] = node
        return node

    def removeNode(self, node):
        if node.data in self.nodes:
            del self.nodes[node.data]

    def addEdge(self, n1, n2, weight):
        if n1 in self.nodes and n2 in self.nodes:
            if n1 not in self.nodes[n2].edges:
                self.nodes[n1].edges[n2] = weight
                self.nodes[n2].edges[n1] = weight

    def removeEdge(self, n1, n2):
        if n1 in self.nodes and n2 in self.nodes:
            if n1 in self.nodes[n2].edges:
                del self.nodes[n1].edges[n2]
                del self.nodes[n2].edges[n1]

    def importFromFile(self, file):
        # clears nodes
        self.nodes = {}

        try:
            with open(file, 'r') as f:
                lines = f.readlines()

            for line in lines:
                line = line.strip()

                if not '--' in line:
                    continue

                parts = line.split('--')
                n1 = parts[0].strip()
                n2 = parts[1].split('[')[0].strip()

                weight = 1
                if '[' in parts[1] and 'weight' in parts[1]:
                    weight = int(parts[1].split('weight=')[1].split(']')[0])

                if n1 not in self.nodes:
                    self.addNode(n1)
                if n2 not in self.nodes:
                    self.addNode(n2)
                self.addEdge(n1, n2, weight)

        except Exception as e:
            # return null if there are errors
            return None
        
    def dfs(self, u):
        u.visited = True
        # print(u.data) 
        for v in u.edges:
            if not self.nodes[v].visited:
                self.dfs(self.nodes[v])

    def init(self):
        for u in self.nodes.values():
            u.visited = False
        for u in self.nodes.values():
            if not u.visited:
                self.dfs(u)

    def printGraph(self):
        for node, graphnode in self.nodes.items():
            print(f"Node {node} has edges: {graphnode.edges}")


        
class Graph2:
    def __init__(self):
        self.nodes = {}
        self.amatrix = {}

    def addNode(self, data):
        node = GraphNode(data)
        self.nodes[data] = node
        for node_data in self.amatrix:
            self.amatrix[node_data][data] = 0
        self.amatrix[data] = {node_data: 0 for node_data in self.nodes}

    def removeNode(self, node):
        if node.data in self.nodes:
            del self.nodes[node.data]
            del self.amatrix[node.data]
            for adj_nodes in self.amatrix.values():
                adj_nodes.pop(node.data, None)

    def addEdge(self, n1, n2, weight):
        if n1 in self.nodes and n2 in self.nodes:
            self.amatrix[n1][n2] = weight
            self.amatrix[n2][n1] = weight

    def removeEdge(self, n1, n2):
        if n1 in self.nodes and n2 in self.nodes:
            self.amatrix[n1].pop(n2, None)
            self.amatrix[n2].pop(n1, None)

    def importFromFile(self, file):
        # clears nodes
        self.nodes = {}
        self.amatrix = {}

        try:
            with open(file, 'r') as f:
                lines = f.readlines()

            for line in lines:
                line = line.strip()

                if not '--' in line:
                    continue

                parts = line.split('--')
                n1 = parts[0].strip()
                n2 = parts[1].split('[')[0].strip()

                weight = 1
                if '[' in parts[1] and 'weight' in parts[1]:
                    weight = int(parts[1].split('weight=')[1].split(']')[0])

                if n1 not in self.nodes:
                    self.addNode(n1)
                if n2 not in self.nodes:
                    self.addNode(n2)
                self.addEdge(n1, n2, weight)

        except Exception as e:
            # return null if there are errors
            return None
        
    def dfs(self, u):
        u.visited = True
        for v in self.amatrix[u.data]:  # use u.data instead of u
            if not self.nodes[v].visited:
                self.dfs(self.nodes[v])


    def init(self):
        for u in self.nodes.values():
            u.visited = False
        for u in self.nodes.values():
            if not u.visited:
                self.dfs(u)
        
    def printGraph(self):
        for node, edges in self.amatrix.items():
            print(f"Node {node} has edges: {edges}")

graph_alist = Graph1()
graph_amatrix = Graph2()
graph_alist.importFromFile("random.dot")
graph_amatrix.importFromFile("random.dot")

alist_times = []
amatrix_times = []

for _ in range(10):
    alist_times.append(timeit.timeit(lambda: graph_alist.init(), number=1))
    amatrix_times.append(timeit.timeit(lambda: graph_amatrix.init(), number=1))

print("Maximum time for dfs on adjacency list graph: ", max(alist_times))
print("Minimum time for dfs on adjacency list graph: ", min(alist_times))
print("Average time for dfs on adjacency list graph: ", sum(alist_times)/len(alist_times))
print("Maximum time for dfs on adjacency matrix graph: ", max(amatrix_times))
print("Minimum time for dfs on adjacency matrix graph: ", min(amatrix_times))
print("Average time for dfs on adjacency matrix graph: ", sum(amatrix_times)/len(amatrix_times))

# dfs on the adjacency list graph is faster, this is because the complexity of DFS on a 
# graph with adjacency list is O(|V| + |E|), where V is the vertices and E is the edges, 
# while the complexity of DFS on a graph with adjacency matrix is O(|V| x |V|).
# This is because dfs() has to go through the entire matrix and check each value, even the ones
# where the value is 0, meaning there's no edge. dfs() does not have to go through every possible edge
# for the graph with adjacency list because the edges that don't exist aren't in the list.
