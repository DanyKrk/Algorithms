#puszczam DFS - jak przetworzę wierzchołek, to go usuwam

from collections import deque


def fill_list_of_neighbours_non_directed(neigh_list, G):
    for x in G:
        if x[1] not in neigh_list[x[0]]:
            neigh_list[x[0]].append(x[1])
        if x[0] not in neigh_list[x[1]]:
            neigh_list[x[1]].append(x[0])

def DFS_delete(neigh_list):
    n = len(neigh_list)
    visited = [False for i in range(n)]
    res = []
    time = 0

    def DFS_visit(u,res, neigh_list):
        visited[u] = True
        for x in neigh_list[u]:
            if visited[x] == False:
                DFS_visit(x,res, neigh_list)
        res.append(u)

    DFS_visit(0,res, neigh_list)
    print(res)

V = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
G = [(0, 1), (1, 2), (2, 3), (4, 9), (5, 8), (7, 2), (6, 7), (1, 0), (0,2),(6,4),(8,9)]
n = len(V)
neigh_list = [[] for i in range(n)]
fill_list_of_neighbours_non_directed(neigh_list, G)

print(neigh_list)
DFS_delete(neigh_list)