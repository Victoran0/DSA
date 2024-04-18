# completed in the graphalgo.py file
def bfs(graph, root):
    queue = []
    discovered = [False] * len(graph.data)

    discovered[root] = True
    queue.append(root)
    idx = 0

    while idx < len(queue):
        # dequeue
        current = queue[idx]
        idx += 1

        # check all edges of current
        for node in graph.data[current]:
            if not discovered[node]:
                discovered[node] = True
                queue.append(node)
    return queue














































