def fill_list_of_neighbours_non_directed(neigh_list, G):
    for x in G:
        if x[1] not in neigh_list[x[0]]:
            neigh_list[x[0]].append(x[1])
        if x[0] not in neigh_list[x[1]]:
            neigh_list[x[1]].append(x[0])


def fill_list_of_neighbours_directed(neigh_list, G):
    for x in G:
        if x[1] not in neigh_list[x[0]]:
            neigh_list[x[0]].append(x[1])

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

def DFS(neigh_list, s):
    n = len(neigh_list)
    visited = [False for i in range(n)]
    entry_time = [None for i in range(n)]
    eop_time = [None for i in range(n)]
    parent = [None for i in range(n)]
    time = 0

    def DFS_visit(u):
        nonlocal time
        time += 1
        visited[u] = True
        entry_time[u] = time

        for x in neigh_list[u]:
            if visited[x] == False:
                parent[x] = u
                DFS_visit(x)

        time += 1
        eop_time[u] = time

    DFS_visit(s)
    print(visited, entry_time, eop_time, parent)


def find_strongly_connected_components(neigh_list):
    def DFS_visit_eop(neigh_list, visited, eop_time, v):
        nonlocal time
        visited[v] = True
        for x in neigh_list[v]:
            if not visited[x]:
                DFS_visit_eop(neigh_list, visited, eop_time, x)
        time += 1
        eop_time[v][1] = time

    def DFS_visit_assign_scc_ids(neigh_list, visited, strongly_connected_component_ids, scc_id, el):
        visited[el] = True
        strongly_connected_component_ids[el] = scc_id
        for x in neigh_list[el]:
            if not visited[x]:
                DFS_visit_assign_scc_ids(neigh_list, visited, strongly_connected_component_ids, scc_id, x)

    n = len(neigh_list)
    visited = [False for i in range(n)]
    eop_time = [[i, -1] for i in range(n)] #tablica z parami[(indeks wierzchołka),(czas przetworzenia)]
    time = 0
    scc_id = 0
    strongly_connected_component_ids = [None for i in range(n)]


    for v in range(n):
        if visited[v] == False: DFS_visit_eop(neigh_list, visited, eop_time, v) #wypełniam tablice z czasami przetworzenia

    quicksort_with_function(eop_time,lambda x: x[1]) #sortuje wierzchołki po czasie przetworzenia

    visited = [False for i in range(n)]
    reversed_neigh_list = [[] for i in range(n)]
    for i in range(n):
        for x in neigh_list[i]:
            reversed_neigh_list[x].append(i)
    for i in range(n-1,-1,-1): #puszczam DFS-a po odwróconych krawędziach po wierzchołkach o malejącym czasie przetworzenia
            if not visited[eop_time[i][0]]:
                DFS_visit_assign_scc_ids(reversed_neigh_list, visited, strongly_connected_component_ids, scc_id, eop_time[i][0])
                scc_id += 1

    print(strongly_connected_component_ids)


V = [0, 1, 2, 3, 4, 5, 6]
G = [(1, 3), (3, 2), (2, 1), (2, 4), (4, 6), (6, 5), (5, 4), (0,1)]
n = len(V)
neigh_list = [[] for i in range(n)]
fill_list_of_neighbours_directed(neigh_list, G)


find_strongly_connected_components(neigh_list)
