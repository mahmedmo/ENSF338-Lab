class GraphNode:
    def __init__(self, data):
        self.data = data
        self.edges = {}

class Graph:
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

    def removeEdge(self, n1, n2):
        if n1 in self.nodes and n2 in self.nodes:
            if n1 in self.nodes[n2].edges:
                del self.nodes[n1].edges[n2]

    def isdag(self):
        visited = set()
        stack = set()

        def dfs(node):
            visited.add(node)
            stack.add(node)

            for neighbor in self.nodes[node].edges:
                if neighbor not in visited:
                    if dfs(neighbor):
                        return True
                elif neighbor in stack:
                    return True

            stack.remove(node)
            return False

        for node in self.nodes:
            if node not in visited:
                if dfs(node):
                    return False

        return True

    def toposort(self):
        if not self.isdag():
            return None

        visited = set()
        stack = []

        def dfs(node):
            visited.add(node)

            for neighbor in self.nodes[node].edges:
                if neighbor not in visited:
                    dfs(neighbor)

            stack.append(node)

        for node in self.nodes:
            if node not in visited:
                dfs(node)

        return stack[::-1]

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

                if n1 not in self.nodes:
                    self.addNode(n1)
                if n2 not in self.nodes:
                    self.addNode(n2)

                weight = 1
                if '[' in parts[1] and 'weight' in parts[1]:
                    weight = int(parts[1].split('weight=')[1].split(']')[0])

                self.addEdge(n1, n2, weight)

        except Exception as e:
            # return null if there are errors
            return None

    def printGraph(self):
        for node, graphnode in self.nodes.items():
            print(f"Node {node} has edges: {graphnode.edges}")

graph1 = Graph()
graph1.addNode('A')
graph1.addNode('B')
graph1.addNode('C')
graph1.addEdge('A', 'B', 1)
graph1.addEdge('B', 'C', 1)

print("Test case 1:")
print("Graph is a DAG:", graph1.isdag())  # True
print("Topological order:", graph1.toposort())  # ['A', 'B', 'C']

# Test case 2: A cyclic graph
graph2 = Graph()
graph2.addNode('A')
graph2.addNode('B')
graph2.addNode('C')
graph2.addEdge('A', 'B', 1)
graph2.addEdge('B', 'C', 1)
graph2.addEdge('C', 'A', 1)

print("\nTest case 2:")
print("Graph is a DAG:", graph2.isdag())  # False
print("Topological order:", graph2.toposort())  # None

# Test case 3: A disconnected graph
graph3 = Graph()
graph3.addNode('A')
graph3.addNode('B')
graph3.addNode('C')

print("\nTest case 3:")
print("Graph is a DAG:", graph3.isdag())  # True
print("Topological order:", graph3.toposort())  # ['A', 'B', 'C']
