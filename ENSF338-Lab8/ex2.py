# QUESTION 1
# Dijkstra's algorithm calculates the shortest paths between nodes in a graph. 
# The efficiency of this algorithm depends how you implement the priority queue it uses. 
# An array with linear search is simple yet time inefficient, having a worst case time complexity of O(v^2). 
# To improve the efficency by a lot, a Min-Heap can be used, which allows for vertex extraction in O(log n). 
# This results in an overall time complexity of O((V+E)log V), which is more ideal for dense graphs. 

# QUESTION 2
import timeit
import heapq
import matplotlib.pyplot as plt

class Graph:
    def __init__(self):
        self.nodes = set()
        self.edges = {}
    
    def add_edge(self, from_node, to_node, weight):
        if from_node not in self.edges:
            self.edges[from_node] = []
        self.edges[from_node].append((to_node, weight))
        self.nodes.add(from_node)
        self.nodes.add(to_node)
    
    def slowSP(self, start):
        distances = {node: float('inf') for node in self.nodes}
        distances[start] = 0
        visited = set()
        
        while visited != self.nodes:
            current_node = None
            for node in self.nodes:
                if node in visited: continue
                if current_node is None or distances[node] < distances[current_node]:
                    current_node = node
            
            if current_node is None: break
            
            visited.add(current_node)
            for neighbor, weight in self.edges.get(current_node, []):
                new_distance = distances[current_node] + weight
                if new_distance < distances[neighbor]:
                    distances[neighbor] = new_distance
        
        return distances
    #  Min-Heap aided by ChatGPT
    def fastSP(self, start):
        distances = {node: float('inf') for node in self.nodes}
        distances[start] = 0
        priority_queue = [(0, start)]
        
        while priority_queue:
            current_distance, current_node = heapq.heappop(priority_queue)
            if current_distance > distances[current_node]:
                continue
            
            for neighbor, weight in self.edges.get(current_node, []):
                new_distance = current_distance + weight
                if new_distance < distances[neighbor]:
                    distances[neighbor] = new_distance
                    heapq.heappush(priority_queue, (new_distance, neighbor))
        
        return distances
    
# QUESTION 3
def load_graph(file_path):
    graph = Graph()
    with open(file_path, 'r') as file:
        for line in file:
            if '--' in line:
                parts = line.split('--')
                from_node = parts[0].strip()
                to_node = parts[1].split('[')[0].strip()
                weight = int(parts[1].split('=')[1].split(']')[0])
                graph.add_edge(from_node, to_node, weight)
                graph.add_edge(to_node, from_node, weight) 
    return graph

# Timing tests aided by ChatGPT
def measure_performance(graph, method_name):
    times = []
    for node in graph.nodes:
        t = timeit.timeit('graph.{}("{}")'.format(method_name, node), globals=globals(), number=1)
        times.append(t)
    return times


graph = load_graph('random.dot')

# Timing tests aided by ChatGPT
slow_times = measure_performance(graph, 'slowSP')
fast_times = measure_performance(graph, 'fastSP')

print("SlowSP - Avg time: {}, Max time: {}, Min time: {}".format(sum(slow_times)/len(slow_times), max(slow_times), min(slow_times)))
print("FastSP - Avg time: {}, Max time: {}, Min time: {}".format(sum(fast_times)/len(fast_times), max(fast_times), min(fast_times)))

# QUESTION 4
# Plotting aided by ChatGPT
plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
plt.hist(slow_times, bins=20, color='skyblue', edgecolor='black')
plt.title('Distribution of Execution Times for slowSP')
plt.xlabel('Execution Time (seconds)')
plt.ylabel('Frequency')

plt.subplot(1, 2, 2)
plt.hist(fast_times, bins=20, color='lightgreen', edgecolor='black')
plt.title('Distribution of Execution Times for fastSP')
plt.xlabel('Execution Time (seconds)')
plt.ylabel('Frequency')

plt.tight_layout()
plt.show()

# Question 4 Discussion
# The histogram for slowSP shows a much higher frequency of longer times in comparison with fastSP, with the average time being 0.06 seconds. 
# This demonstrates the ineffiency of the algorithim used for slowSP (the array with linear search). 
# However, fastSP, utilizes a Min-Heap, a more optimized algorithm/data structure for this task, than what was used previously. 
# This is evident in the results, as fastSP displayed results much faster stemming from 0.0012 seconds to as long as 0.0016 seconds. 
# fastSP had a larger spread in results than slowSP, but was shwon to be signifcantly faster than slowSP. 