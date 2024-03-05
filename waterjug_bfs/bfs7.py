from collections import deque

def BFS(a, b, target):

    m = {}
    isSolvable = False
    path = []
    q = deque()
    q.append((0, 0))

    while len(q) > 0:
        u = q.popleft()
        if (u[0], u[1]) in m:
            continue
        if (u[0] > a or u[1] > b or u[0] < 0 or u[1] < 0):
            continue

        path.append([u[0], u[1]])
        m[(u[0], u[1])] = 1

        if u[0] == target or u[1] == target:
            isSolvable = True

            if u[0] == target:
                if u[1] != 0:
                    path.append([u[0], 0])
            else:
                if u[0] != 0:
                    path.append([0, u[1]])

            sz = len(path)
            for i in range(sz):
                print("(", path[i][0], ",", path[i][1], ")")
            break
        elif u[0] + u[1] == target:
            isSolvable = True
            sz = len(path)
            for i in range(sz):
                print("(", path[i][0], ",", path[i][1], ")")
            break

        # Fill jug operations
        q.append([a, u[1]])
        q.append([u[0], b])

        # Empty jug operations
        q.append([0, u[1]])
        q.append([u[0], 0])

        # Pour water from one jug to another
        pour = min(u[0], b - u[1])
        q.append([u[0] - pour, u[1] + pour])

        pour = min(a - u[0], u[1])
        q.append([u[0] + pour, u[1] - pour])

    if not isSolvable:
        print("No solution")

if __name__ == '__main__':
    Jug1, Jug2, target = 4, 5, 7
    print("Path from initial state to solution state ::")
    BFS(Jug1, Jug2, target)
