from collections import deque


def fill_list_of_neighbours_non_directed(neigh_list, G):
    for x in G:
        if x[1] not in neigh_list[x[0]]:
            neigh_list[x[0]].append(x[1])
        if x[0] not in neigh_list[x[1]]:
            neigh_list[x[1]].append(x[0])

def find_bridges(neigh_list):
    def DFS_visit(bridges, neigh_list, visited, parent,entry_time,low, el):
        print(el, end = " ")
        nonlocal time
        time += 1
        entry_time[el] = time
        low[el] = time
        visited[el] = True
        for x in neigh_list[el]:
            if not visited[x]:
                parent[x] = el
                DFS_visit(bridges, neigh_list, visited, parent, entry_time,low, x)
        for x in neigh_list[el]:
            if parent[x] == el:
                low[el] = min(low[el], low[x])
            elif parent[el] != x:
                low[el] = min(low[el], low[x])
        if entry_time[el] == low[el] and parent[el] != None:
            bridges.append((parent[el],el))

    n = len(neigh_list)
    bridges = []
    visited = [False for i in range(n)]
    parent = [None for i in range(n)]
    entry_time = [None for i in range(n)]
    low = [None for i in range(n)]
    time = 0
    DFS_visit(bridges,neigh_list,visited,parent,entry_time,low,0)
    print(bridges)
    print(low)





# V = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# G = [(0, 1), (1, 2), (2, 3), (4, 9), (5, 8), (7, 2), (6, 7), (1, 0), (0, 2), (6, 4), (8, 9), (3, 5)]
V = [0, 1, 2, 3, 4, 5, 6]
G = [(1, 3), (3, 2), (2, 1), (2, 4), (4, 6), (6, 5), (5, 4), (0,1), (3,6)]
n = len(V)
neigh_list = [[] for i in range(n)]
fill_list_of_neighbours_non_directed(neigh_list, G)
find_bridges(neigh_list)
