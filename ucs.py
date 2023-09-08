import heapq

class Graph:
    def __init__(self):
        self.vertices = {}

    def add_edge(self, from_vertex, to_vertex, weight):
        if from_vertex not in self.vertices:
            self.vertices[from_vertex] = []
        if to_vertex not in self.vertices:
            self.vertices[to_vertex] = []
        self.vertices[from_vertex].append((to_vertex, weight))
        self.vertices[to_vertex].append((from_vertex, weight))  # For undirected graph

    def uniform_cost_search(self, start, goal):
        frontier = [(0, start)]  # (cost, vertex)
        visited = set()
        parent = {}  # Store parent vertices for path reconstruction

        while frontier:
            cost, current = heapq.heappop(frontier)

            if current == goal:
                # Reconstruct the path from start to goal
                path = []
                while current != start:
                    path.append(current)
                    current = parent[current]
                path.append(start)
                path.reverse()
                return cost, path

            if current in visited:
                continue

            visited.add(current)

            for neighbor, weight in self.vertices.get(current, []):
                if neighbor not in visited:
                    heapq.heappush(frontier, (cost + weight, neighbor))
                    parent[neighbor] = current

        return None, []

def build_graph():
    graph = Graph()

    graph.add_edge("S", "A", 1)
    graph.add_edge("S", "B", 4)
    graph.add_edge("A", "C", 3)
    graph.add_edge("A", "D", 2)
    graph.add_edge("B", "G1", 5)
    graph.add_edge("C", "E", 5)
    graph.add_edge("D", "F", 1)
    graph.add_edge("D", "G2", 3)
    graph.add_edge("E", "G3", 5)

    return graph

if __name__ == "__main__":
    graph = build_graph()
    print("Graph:")
    for vertex, neighbors in graph.vertices.items():
        print(f"{vertex}: {neighbors}")

    start_state = input("Enter the start state: ")
    goal_state = input("Enter the goal state: ")

    if start_state not in graph.vertices or goal_state not in graph.vertices:
        print("Invalid start or goal state.")
    else:
        shortest_path_cost, shortest_path = graph.uniform_cost_search(start_state, goal_state)
        if shortest_path_cost is not None:
            print(f"Shortest path cost from {start_state} to {goal_state}: {shortest_path_cost}")
            print("Shortest path chosen:", " -> ".join(shortest_path))
        else:
            print(f"There is no path from {start_state} to {goal_state}.")
