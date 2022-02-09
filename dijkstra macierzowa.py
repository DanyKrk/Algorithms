from math import inf
#G - macierz sąsiedztwa ()

def convert_list_of_non_directed_veighted_edges_to_matrix(L):
    max_n = -1
    for edge in L:
        max_n = max(edge[0],max_n)
        max_n = max(edge[1], max_n)

    n = max_n + 1
    G = [[-1]*n for i in range(n)]

    for edge in L:
        G[edge[0]][edge[1]] = edge[2]
        G[edge[1]][edge[0]] = edge[2]

    return G


def Dijkstra(G, s):
    n = len(G)
    visited = [False for i in range(n)]
    distance = [inf for i in range(n)]
    parent = [-1 for i in range(n)]

    present_id = s
    distance[s] = 0
    while True:
        visited[present_id] = True
        next_v_id = -1
        next_v_dist = inf

        #znajdowanie krawędzi lekkiej
        for i in range(n):
            if visited[i]: continue
            #aktualizuje minimalne odleglosci od S dla wierzchołków do których moge dojsc z present
            if G[present_id][i] != -1 and distance[i] > distance[present_id] + G[present_id][i]:
                distance[i] = distance[present_id] + G[present_id][i]
                parent[i] = present_id
            #wybieram nastepny wierzhołek
            if next_v_dist > distance[i]:
                next_v_id = i
                next_v_dist = distance[i]

        if next_v_id == -1: return distance, parent #odwiedziłem wszystkie wierzchołki (do których mozna dotrzec z wierzchołka 0 - NIE SPRAWDZAM SPÓJNOŚCI)

        present_id = next_v_id

L = [(1, 2, 4), (0, 5, 9), (4, 3, 5), (3, 5, 3), (2, 5, 1),(2,3,100),(0,3,34),(1,3,89)]
G = convert_list_of_non_directed_veighted_edges_to_matrix(L)
print(G)
print(Dijkstra(G, 0))


