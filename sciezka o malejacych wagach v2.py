from queue import PriorityQueue


class Edge:
    def __init__(self, dest, wag, idx):
        self.dest = dest
        self.wag = wag
        self.idx = idx
        self.par = -1



def check(G, s, t):
    n = len(G)
    E = []
    pos = [0] * n     # tablica liczników krawędzi wychodzących dla każdego wierzchołka
    cnt = 0
    for i in range(n):
        G[i].sort(key=lambda x: x[1])
        for j in range(len(G[i])):
            E.append(Edge(G[i][j][0], G[i][j][1], cnt))     # v docelowy, waga, numer krawędzi
            G[i][j] = cnt                        # podmieniamy krotkę z krawędzią na jej numer
            cnt += 1

    P = PriorityQueue()
    for i in G[s]:
        P.put((E[i].wag, E[i].idx))
        pos[s] += 1

    res = -1
    last = -1
    while P.qsize() > 0:
        cost, edge = P.get()

        v = E[edge].dest  # wierzchołek docelowy

        # idziemy po kolejnych krawędziach wychodzących, dopóki spełniona jest monoticzność
        while pos[v] < len(G[v]) and E[G[v][pos[v]]].wag < E[edge].wag:
            next = G[v][pos[v]]  # numer kolejnej krawędzi
            E[next].par = edge
            P.put((cost + E[next].wag, next))  # wstawienie kolejnej krawędzi do kolejki
            pos[v] += 1

        if v == t:
            last = edge
            res = cost
            break

    A = [s]

    def printing(x):
        if E[x].par != -1:
            printing(E[x].par)
        A.append(E[x].dest)

    printing(last)
    return res, A


G1 = [
    [[2, 100], [1, 4]],  # 0
    [[0, 4], [4, 3]],  # 1
    [[3, 200], [0, 100], [4, 4]],  # 2
    [[2, 200], [4, 3]],  # 3
    [[2, 4], [1, 3], [3, 3]]  # 4
]
print(check(G1, 0, 3))


G2 = [[(1, 6), (2, 7), (3, 8), (4, 12)],
      [(0, 6), (3, 3)],
      [(0, 7), (4, 3)],
      [(1, 3), (0, 8), (4, 2), (5, 4)],
      [(0, 12), (2, 3), (3, 2), (5, 2)],
      [(3, 4), (4, 2)]]
print(check(G2, 0, 5))