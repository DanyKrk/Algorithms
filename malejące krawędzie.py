from collections import deque


def fill_list_of_neighbours_non_directed_with_weigths(neigh_list, G): #w listach sąsiedztwa krotki (nr_sąsiada, waga krawedzi do niego)
    n = len(G)
    for i in range(n):
        if G[i][1] not in neigh_list[G[i][0]]:
            neigh_list[G[i][0]].append((G[i][1],W[i]))
            neigh_list[G[i][1]].append((G[i][0],W[i]))


def DFS_decreasing_weights_x_to_y(ad_list,x,y):
    def DFS_visit(ad_list, el, in_weight, y):
        if el == y:
            return True
        visited[el] = True
        for neigh in ad_list[el]:
            if visited[neigh[0]] == False and neigh[1]<in_weight:
                if DFS_visit(ad_list, neigh[0],neigh[1],y):
                    return True
        return False

    n = len(ad_list)
    visited = [False for i in range(n)]
    for el in neigh_list[x]:
        if DFS_visit(ad_list,el[0],el[1], y):
            return True
    return False



V = [0, 1, 2, 3, 4, 5, 6, 7]
G = [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (3, 7), (6, 7)]
W = [10,      9,       8,      10,        6,    5,       10,      3]
n = len(V)
neigh_list = [[] for i in range(n)]
fill_list_of_neighbours_non_directed_with_weigths(neigh_list, G)

print(DFS_decreasing_weights_x_to_y(neigh_list,0,6))