
# Create a class to represent a graph as an adjacency list in python

# class Graph:
#     def __init__(self, num_nodes, edges):
#         self.num_nodes = num_nodes
#         self.data = [[] for _ in range(num_nodes)]
#         for n1, n2 in edges:
#             # Insert into the right lists
#             self.data[n1].append(n2)
#             self.data[n2].append(n1)
#
#     def __repr__(self):
#         return "\n".join(["{}: {}".format(n, neighbors) for n, neighbors in enumerate(self.data)])
#
#     def __str__(self):
#         return self.__repr__()


# Breadth first search

def bfs(graph, root):
    queue = []
    discovered = [False] * len(graph.data)
    distance = [None] * len(graph.data)
    parent = [None] * len(graph.data)

    discovered[root] = True
    queue.append(root)
    distance[root] = 0
    idx = 0

    while idx < len(queue):
        # dequeue
        current = queue[idx]
        idx += 1

        # check all edges of current
        for node in graph.data[current]:
            if not discovered[node]:
                distance[node] = 1 + distance[current]
                parent[node] = current
                discovered[node] = True
                queue.append(node)
    return queue, distance, parent


# Depth first search
def dfs(graph, root):
    stack = []
    discovered = [False] * len(graph.data)
    result = []

    stack.append(root)

    while len(stack) > 0:
        current = stack.pop()
        if not discovered[current]:
            discovered[current] = True
            result.append(current)
            for node in graph.data[current]:
                if not discovered[node]:
                    stack.append(node)

    return result


# A class to represent weighted and directed graphs in python
class Graph:
    def __init__(self, num_nodes, edges, directed=False, weighted=False):
        self.num_nodes = num_nodes
        self.directed = directed
        self.weighted = weighted
        self.data = [[] for _ in range(num_nodes)]
        self.weight = [[] for _ in range(num_nodes)]
        for edge in edges:
            if self.weighted:
                # include weights
                node1, node2, weight = edge
                self.data[node1].append(node2)
                self.weight[node1].append(weight)
                if not directed:
                    self.data[node2].append(node1)
                    self.weight[node2].append(weight)
            else:
                # work without weights
                node1, node2 = edge
                self.data[node1].append(node2)
                if not directed:
                    self.data[node2].append(node1)

    def __repr__(self):
        result = ""
        if self.weighted:
            for i, (nodes, weights) in enumerate(zip(self.data, self.weight)):
                result += "{}: {}\n".format(i, list(zip(nodes, weights)))
        else:
            for i, nodes in enumerate(self.data):
                result += "{}: {}\n".format(i, nodes)
        return result


def update_distances(graph, current, distance, parent=None):
    # Update the distances of the current node's neighbors
    neighbors = graph.data[current]
    weights = graph.weight[current]
    for i, node in enumerate(neighbors):
        weight = weights[i]
        if distance[current] + weight < distance[node]:
            distance[node] = distance[current] + weight
            if parent:
                parent[node] = current


def pick_next_node(distance, visited):
    # Pick the next unvisited node at the smallest distance
    min_distance = float('inf')
    min_node = None
    for node in range(len(distance)):
        if not visited[node] and distance[node] < min_distance:
            min_node = node
            min_distance = distance[node]
    return min_node


def shortest_path(graph, source, target):
    visited = [False] * len(graph.data)
    parent = [None] * len(graph.data)
    distance = [float('inf')] * len(graph.data)
    queue = []

    distance[source] = 0
    queue.append(source)
    idx = 0

    while idx < len(queue) and not visited[target]:
        current = queue[idx]
        visited[current] = True
        idx += 1

        # Update the distance of all the neighbors
        update_distances(graph, current, distance, parent)

        # Find the first unvisited node with the smallest distance
        next_node = pick_next_node(distance, visited)
        if next_node:
            queue.append(next_node)

    return distance[target], parent


num_nodes = 5
edges = [[0, 1], [0, 4], [1, 2], [1, 3], [1, 4], [2, 3], [3, 4]]
graph1 = Graph(num_nodes, edges)

num_nodes1 = 9
edges1 = [(0, 1, 3), (0, 3, 2), (0, 8, 4), (1, 7, 4), (2, 7, 2), (2, 3, 6), (2, 5, 1), (3, 4, 1), (4, 8, 8), (5, 6, 8)]
graph2 = Graph(num_nodes1, edges1, weighted=True)

num_nodes6 = 5
edges6 = [(0, 1), (1, 2), (2, 3), (2, 4), (4, 2), (3, 0)]
graph3 = Graph(num_nodes6, edges6, directed=True)

num_nodes7 = 6
edges7 = [(0, 1, 4), (0, 2, 2), (1, 2, 5), (1, 3, 10), (2, 4, 3), (4, 3, 4), (3, 5, 11)]
graph4 = Graph(num_nodes7, edges7, weighted=True, directed=True)

sh = shortest_path(graph4, 0, 5)

sp = shortest_path(graph2, 2, 8)

print(sp)





















































