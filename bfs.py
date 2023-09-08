def bfs(graph, start, goal):
    visited = set()
    queue = [[start]]
    while queue:
        path = queue.pop(0)
        node = path[-1]
        if node not in visited:
            neighbours = graph[node]
            for neighbour in neighbours:
                new_path = list(path)
                new_path.append(neighbour)
                queue.append(new_path)
                if neighbour == goal:
                    return new_path
            visited.add(node)

graph = {'A': ['B', 'C'],
         'B': ['D', 'E'],
         'C': ['F', 'G']}

print("The graph is: ", graph)
goal_state = input("Enter the goal state: ")
shortest_path = bfs(graph, 'A', goal_state)
print("The shortest path from A to", goal_state, "is:", shortest_path)
