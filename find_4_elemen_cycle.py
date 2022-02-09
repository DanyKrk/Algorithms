def fill_tab_of_neighbours_non_directed(neigh_list, G):
    for x in G:
        neigh_list[x[0]][x[1]] = 1
        neigh_list[x[1]][x[0]] = 1


def find_4_cycle(G):
    n = len(G)
    neigh_tab = [[0] * n for i in range(n)]
    fill_tab_of_neighbours_non_directed(neigh_tab, G)

    for x in range(n):
        for y in range(n):
            if x == y: continue
            same_neighbours_number = 0
            same_neighbours=[-1,-1]
            for i in range(n):
                if neigh_tab[x][i] == 1:
                    if neigh_tab[y][i] == 1:
                        same_neighbours_number += 1
                        same_neighbours[same_neighbours_number%2] = i

            if same_neighbours_number >= 2:
                print(x,same_neighbours[0],y,same_neighbours[1])
#                return True
        return False

V = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
G = [(0, 1), (1, 2), (2, 3), (4, 9), (5, 8), (7, 2), (6, 7), (1, 0), (0,2),(6,4),(8,9), (3,1)]
G = [(0,1), (0,2), (0,3), (1,2), (1, 3), (2,3), (0,0),(1,1),(2,2)]
find_4_cycle(G)