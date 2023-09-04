from collections import deque

def water_jug_problem(jug1_capacity, jug2_capacity, target_liters):
    visited = set()
    queue = deque([(0, 0, [])])  # Initial state: both jugs empty

    while queue:
        jug1, jug2, actions = queue.popleft()

        if jug1 == target_liters or jug2 == target_liters:
            return actions
        
        if (jug1, jug2) in visited:
            continue

        visited.add((jug1, jug2))

        # Fill jug 1
        if jug1 < jug1_capacity:
            queue.append((jug1_capacity, jug2, actions + ['Fill Jug 1']))

        # Fill jug 2
        if jug2 < jug2_capacity:
            queue.append((jug1, jug2_capacity, actions + ['Fill Jug 2']))

        # Empty jug 1
        if jug1 > 0:
            queue.append((0, jug2, actions + ['Empty Jug 1']))

        # Empty jug 2
        if jug2 > 0:
            queue.append((jug1, 0, actions + ['Empty Jug 2']))

        # Pour from jug 1 to jug 2
        pour_amount = min(jug1, jug2_capacity - jug2)
        if pour_amount > 0:
            queue.append((jug1 - pour_amount, jug2 + pour_amount, actions + ['Pour Jug 1 -> Jug 2']))

        # Pour from jug 2 to jug 1
        pour_amount = min(jug2, jug1_capacity - jug1)
        if pour_amount > 0:
            queue.append((jug1 + pour_amount, jug2 - pour_amount, actions + ['Pour Jug 2 -> Jug 1']))

    return None  # No solution found

# Example usage
jug1_capacity = int(input("Enter the capacity of jug 1: "))
jug2_capacity = int(input("Enter the capacity of jug 2: "))
target_liters = int(input("Enter the target amount to achieve: "))
solution = water_jug_problem(jug1_capacity, jug2_capacity, target_liters)

if solution:
    # print(solution)
    for step, action in enumerate(solution):
        print(f"Step {step + 1}: {action}")
else:
    print("No solution found.")
