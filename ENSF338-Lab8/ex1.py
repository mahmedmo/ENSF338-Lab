
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

    def printGraph(self):
        for node, graphnode in self.nodes.items():
            print(f"Node {node} has edges: {graphnode.edges}")