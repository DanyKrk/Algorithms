from collections import deque


def convert_list_of_directed_edges_to_matrix(L):
    max_n = -1
    for edge in L:
        max_n = max(edge[0],max_n)
        max_n = max(edge[1], max_n)

    n = max_n + 1
    G = [[0]*n for i in range(n)]

    for edge in L:
        G[edge[0]][edge[1]] = 1

    return G

def quicksort_with_function(tab, f):  # wersja z funcją po czym sortować
    def partition(tab, b, e, f):
        x = f(tab[e])
        i = b - 1
        for j in range(b, e):
            if f(tab[j]) <= x:
                i += 1
                tab[i], tab[j] = tab[j], tab[i]
        tab[i + 1], tab[e] = tab[e], tab[i + 1]
        return i + 1

    def quicksort_int(tab, b, e, f):
        while b < e:
            q = partition(tab, b, e, f)
            if q - b < e - q:
                quicksort_int(tab, b, q - 1, f)
                b = q + 1
            else:
                quicksort_int(tab, q + 1, e, f)
                e = q - 1

    n = len(tab)
    quicksort_int(tab, 0, n - 1, f)

def DFS_matrix_returning_eop_time(G, s): #G - macierz sąsiedztwa
    n = len(G)
    visited = [False for i in range(n)]
    eop_time = [[None,i] for i in range(n)]
    time = 0

    def DFS_visit(u):
        nonlocal time
        time += 1
        visited[u] = True

        for x in range(n):
            if G[u][x] == 1 and visited[x] == False:
                DFS_visit(x)

        time += 1
        eop_time[u][0] = time

    DFS_visit(s)
    return eop_time

def DFS_matrix_assignig_SCC_using_invertet_edges(G, eop_time, strongly_conected_components): #G - macierz sąsiedztwa
    n = len(G)
    visited = [False for i in range(n)]
    time = 0

    def DFS_visit_SCC(u, i):
        visited[u] = True
        strongly_conected_components[u] = i

        for x in range(n):
            if G[x][u] == 1 and visited[x] == False:
                DFS_visit_SCC(x,i)


    for i in range(n-1,-1,-1):
        if not visited[eop_time[i][1]]:
            DFS_visit_SCC(eop_time[i][1],eop_time[i][1])


def SSS(G):
    eop_time = DFS_matrix_returning_eop_time(G,0)
    quicksort_with_function(eop_time,lambda x:x[0])
    strongly_conected_component = [-1]*len(G)
    DFS_matrix_assignig_SCC_using_invertet_edges(G, eop_time, strongly_conected_component)
    print(strongly_conected_component)

L = ((0,1),(0,4), (1,2), (2,0), (1,3), (3,4), (4,5), (5,3), (5,6), (6,3), (2,7), (7,9), (8, 7), (8,6), (9,10), (10,8))

print(convert_list_of_directed_edges_to_matrix(L))
SSS(convert_list_of_directed_edges_to_matrix(L))


