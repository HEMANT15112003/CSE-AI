from collections import deque


def BFS(a, b, target):
    m = {}
    isSolvable = False
    path = []

    q = deque()

    q.append((0, 0))

    while len(q) > 0:
        u = q.popleft()  # If this state is already visited
        if (u[0], u[1]) in m:
            continue
        if u[0] > a or u[1] > b or u[0] < 0 or u[1] < 0:
            continue

        # Filling the vector for constructing
        # the solution path
        path.append([u[0], u[1]])

        # Marking current state as visited
        m[(u[0], u[1])] = 1

        # If we reach the solution state, put ans=1
        if u[0] == target or u[1] == target:
            isSolvable = True

            if u[0] == target:
                if u[1] != 0:
                    # Fill final state
                    path.append([u[0], 0])
            else:
                if u[0] != 0:
                    # Fill final state
                    path.append([0, u[1]])

            # Print the solution path
            sz = len(path)
            for i in range(sz):
                print("(", path[i][0], ",", path[i][1], ")")
            break

        # If we have not reached the final state
        # then, start developing intermediate
        # states to reach the solution state

        # Fill Jug2
        if u[1] < b:
            q.append([u[0], b])

        # Fill Jug1
        if u[0] < a:
            q.append([a, u[1]])

        # Pour water from Jug1 to Jug2
        if u[0] > 0 and u[1] < b:
            pour = min(u[0], b - u[1])
            q.append([u[0] - pour, u[1] + pour])

        # Pour water from Jug2 to Jug1
        if u[1] > 0 and u[0] < a:
            pour = min(u[1], a - u[0])
            q.append([u[0] + pour, u[1] - pour])

        # Empty Jug2
        if u[1] > 0:
            q.append([u[0], 0])

        # Empty Jug1
        if u[0] > 0:
            q.append([0, u[1]])

    # No solution exists if ans=0
    if not isSolvable:
        print("No solution")


# Driver code
if __name__ == '__main__':
    Jug1 = int(input("Enter the capacity of Jug1: "))
    Jug2 = int(input("Enter the capacity of Jug2: "))
    target = int(input("Enter the target amount: "))
    print("Path from initial state "
          "to solution state ::")

    BFS(Jug1, Jug2, target)
