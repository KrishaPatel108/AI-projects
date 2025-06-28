from collections import deque

def bfs_shortest_path(graph, start, goal):
    visited = set()
    queue = deque([[start]])  # store paths, not just nodes

    if start == goal:
        return [start]

    while queue:
        path = queue.popleft()
        node = path[-1]

        if node not in visited:
            neighbours = graph.get(node, [])

            for neighbour in neighbours:
                new_path = list(path)
                new_path.append(neighbour)
                queue.append(new_path)

                if neighbour == goal:
                    return new_path

            visited.add(node)

    return None

city_map = {
    'ReliefCentre': ['A', 'B'],
    'A': ['C', 'D'],
    'B': ['E'],
    'C': [],
    'D': ['VictimArea'],
    'E': ['D'],
    'VictimArea': []
}

# Test the function
path = bfs_shortest_path(city_map, 'ReliefCentre', 'VictimArea')
print("Optimal rescue path:", path)

city_map_2 = {
    'ReliefCentre': ['X', 'Y'],
    'X': ['A', 'B'],
    'Y': ['C'],
    'A': ['D'],
    'B': ['E', 'F'],
    'C': ['G'],
    'D': ['VictimArea'],
    'E': ['VictimArea'],
    'F': ['H'],
    'G': ['H'],
    'H': ['VictimArea'],
    'VictimArea': []
}

# Test with the new map
path = bfs_shortest_path(city_map_2, 'ReliefCentre', 'VictimArea')
print("Optimal rescue path (Map 2):", path)
