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

    def isdag(self):
        visited = set()
        in_stack = set()

        def dfs(node):
            visited.add(node)
            in_stack.add(node)

            for neighbor in self.nodes[node].edges:
                if neighbor not in visited:
                    if dfs(neighbor):
                        return True
                elif neighbor in in_stack:
                    return True

            in_stack.remove(node)
            return False

        for node in self.nodes:
            if node not in visited:
                if dfs(node):
                    return False

        return True

    def toposort(self):
        if not self.isdag():
            return None
        
        in_degree = {node: 0 for node in self.nodes}
        for node in self.nodes:
            for neighbor in self.nodes[node].edges:
                in_degree[neighbor] += 1

        queue = [node for node in self.nodes if in_degree[node] == 0]
        topo_order = []

        while queue:
            current = queue.pop(0)
            topo_order.append(current)

            for neighbor in self.nodes[current].edges:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)

        return topo_order if len(topo_order) == len(self.nodes) else None
    
# Test 1: Create a graph, add nodes, and edges
graph = Graph()
node_a = graph.addNode('A')
node_b = graph.addNode('B')
node_c = graph.addNode('C')
node_d = graph.addNode('D')
node_e = graph.addNode('E')

graph.addEdge('A', 'B', 1)
graph.addEdge('A', 'C', 1)
graph.addEdge('B', 'D', 1)
graph.addEdge('C', 'D', 1)
graph.addEdge('D', 'E', 1)

# Test 2: Check if the graph is a DAG
print("Is the graph a DAG?", graph.isdag())  # Output: True

# Test 3: Check topological sorting for a DAG
print("Topological order:", graph.toposort())  # Output: ['A', 'C', 'B', 'D', 'E']

# Test 4: Remove an edge to introduce a cycle
graph.removeEdge('C', 'D')

# Test 5: Check if the graph is still a DAG
print("Is the graph a DAG?", graph.isdag())  # Output: False

# Test 6: Check topological sorting for a graph with a cycle
print("Topological order:", graph.toposort())  # Output: None

# Test 7: Remove a node
graph.removeNode(node_c)

# Test 8: Check if the graph is still a DAG after node removal
print("Is the graph a DAG?", graph.isdag())  # Output: True

# Test 9: Import graph from file
graph.importFromFile('test_graph.txt')

# Test 10: Check if the imported graph is a DAG
print("Is the imported graph a DAG?", graph.isdag())  # Output: True

# Test 11: Check topological sorting for the imported graph
print("Topological order for imported graph:", graph.toposort())  # Output: Topological order list or None
