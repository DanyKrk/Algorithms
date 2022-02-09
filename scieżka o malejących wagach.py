from queue import PriorityQueue

def find_decreasing_path(neigh_list,b,e): # neigh_list - lista sąsiadztwa  - krotki (waga_krawędzi, id_sąsiada)
    n = len(neigh_list)
    for i in range(n): # sortuje listy sąsiedztwa malejąco po wagach
        neigh_list[i].sort(reverse=True, key=lambda x:x[0])

    P = PriorityQueue() #trzymam tu krotki (odległość od s, waga krawędzi po której wchodzę, id wierzchołka do którego wchodze)

    for neigh in neigh_list[b]:
        P.put((neigh[0],neigh[0],neigh[1]))

    while P:
        el = P.get()
        u = el[2]
        w = el[1]
        d = el[0]

        if u == e:
            return d

        n = len(neigh_list[u])
        i = n-1
        while i >= 0 and neigh_list[u][i][0] < w:
            neigh = neigh_list[u].pop()
            P.put((d+neigh[0],neigh[0],neigh[1]))
            i -= 1


neigh_list = [[(8,1),(5,5)],[(8,0),(2,4),(1,2)],[(1,1),(2,4),(1,3)],[(1,2),(4,4)],[(4,3),(2,2),(2,1),(3,5)],[(3,4),(5,0)]]
print(find_decreasing_path(neigh_list,0,3))