from collections import deque
def find_shortest_dist_from_x_to_y(adjacency_matrix, x, y):
    n = len(adjacency_matrix)
    visited = [False for i in range(n)]
    parent = [None for i in range(n)]
    Q = deque()
    Q.append(x)
    while Q:
        u = Q.popleft()
        visited[u] = True
        for i in range(n):
            if adjacency_matrix[u][i] >= 0 and visited[u] == False:
