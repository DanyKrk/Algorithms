from collections import deque
from math import inf


def find_extending_path(R, s, t):
    n = len(R)
    Q = deque()
    visited = [False] * n
    parent = [-1] * n
    min_capacity_in_path = [inf] * n
    path = []

    visited[s] = True
    Q.append(s)
    while Q:
        u = Q.popleft()
        for v in range(n):
            if R[u][v] != 0 and visited[v] == False:
                parent[v] = u
                visited[v] = True
                min_capacity_in_path[v] = min(min_capacity_in_path[parent[v]], R[u][v])
                if v == t:
                    el = t
                    path.append(t)
                    while el != s:
                        path.append(parent[el])
                        el = parent[el]
                    return path, min_capacity_in_path[t]
                Q.append(v)
    return None, None


def max_flow(G, s, t):
    n = len(G)
    R = [[0] * n for i in range(n)]  # sieć residualna
    F = [[0] * n for i in range(n)]  # przepływ
    flow_capacity = 0

    for i in range(n):
        for j in range(n):
            R[i][j] = G[i][j]

    while True:
        path, extending_capacity = find_extending_path(R, s, t)  # w path  kolejnosc wierzchołłków jest odwrotna do przepływu

        if path == None: return F, flow_capacity

        flow_capacity += extending_capacity
        l = len(path)
        for u_id in \
                range(l - 1, 0, -1):
            u = path[u_id]
            v = path[u_id - 1]

            # ściezka cofa przepływ
            if G[u][v] == 0:
                F[v][u] -= extending_capacity
                R[v][u] += extending_capacity
                R[u][v] -= extending_capacity

            else:  # sciezka zwiększa przepływ
                F[u][v] += extending_capacity
                R[u][v] -= extending_capacity
                R[v][u] += extending_capacity


G = [[0, 5, 0, 0, 0, 6, 3, 0],
     [0, 0, 2, 0, 0, 0, 0, 0],
     [0, 0, 0, 4, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 4, 1, 0, 0, 0, 0],
     [0, 0, 3, 0, 7, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 3],
     [0, 0, 2, 2, 0, 0, 0, 0]]

print(max_flow(G, 0, 3))
