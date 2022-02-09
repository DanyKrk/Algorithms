from collections import deque


def fill_list_of_neighbours_non_directed(neigh_list, G):
    for x in G:
        if x[1] not in neigh_list[x[0]]:
            neigh_list[x[0]].append(x[1])
        if x[0] not in neigh_list[x[1]]:
            neigh_list[x[1]].append(x[0])



def check_bipartition(neigh_list):
    n = len(neigh_list)

    parent = [-1 for i in range(n)]
    visited = [False     for i in range(n)]
    side = [-1 for i in range(n)]
    Q = deque()

    visited[0] = True
    side[0] = 0
    Q.append(0)

    while Q:
        u = Q.popleft()
        for neigh in neigh_list[u]:
            if visited[neigh]:
                if side[neigh] == side[u]:
                    return False
            else:
                visited[neigh] = True
                parent[neigh] = u
                side[neigh] = 1-side[u]
                Q.append(neigh)

    return True

V = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
G = [(0, 1), (1, 2), (2, 3), (4, 9), (5, 8), (7, 2), (6, 7), (1, 0), (0,2)]
n = len(V)
neigh_list = [[] for i in range(n)]
fill_list_of_neighbours_non_directed(neigh_list, G)

print(check_bipartition(neigh_list))
