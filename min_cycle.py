#Daniel Krzykawski
#Odpalam algorytm dijkstry z każdego wierzchołka i analizuje cykle których fragmentem jest wierzchołek z którego puszczam algorytm.
# Jeżeli trafie na 2 wierzchołki, do których dotarłem różnymi ścieżkami i między którymi jest krawędź, to porównuje długość otrzymanego kandydata na cykl
# z minimalną długością cyklu jaką otrzymalem wczesniej.
# Algorytm zaczynający z i znajduje oprócz właściwych cykli fałszywe cykle (takie do których i nie należy), ale to nie jest problem, ponieważ waga
# takiego fałszywego cyklu będzie większa niż waga tego samego cyklu, ale analizowanego z wierzchołka który do niego należy.

from copy import deepcopy
from math import inf
from collections import deque

def min_cycle( G ):
    n = len(G)

    min_cycle_parent = []
    min_cycle_length = inf
    min_cycle_a = 0
    min_cycle_b = 0
    for i in range(n):
        distance = [inf for i in range(n)]
        visited = [False for i in range(n)]
        parent = [-1 for i in range(n)]
        parent[i] = i
        distance[i] = 0
        next_v = i
        next_distance = inf
        for _ in range(n):
            present = next_v
            next_distance = inf
            visited[present] = True
            for j in range(n):
                if G[present][j] != -1 and visited[j] == True and parent[present] != j:
                    if distance[j] + distance[present] + G[present][j] < min_cycle_length:
                        min_cycle_length = distance[j] + distance[present] + G[present][j]
                        min_cycle_parent = parent.copy()
                        min_cycle_a = present
                        min_cycle_b = j

                if G[present][j] != -1 and visited[j] == False:
                    if distance[j] > distance[present] + G[present][j]:
                        distance[j] = distance[present] + G[present][j]
                        parent[j] = present

                if visited[j] == False and distance[j] < next_distance:
                    next_v = j
                    next_distance = distance[j]
    res = deque()
    res_l =[]
    while min_cycle_parent[min_cycle_a] != min_cycle_a:
        res.appendleft(min_cycle_a)
        min_cycle_a = min_cycle_parent[min_cycle_a]
    while min_cycle_parent[min_cycle_b] != min_cycle_b:
        res.append(min_cycle_b)
        min_cycle_b = min_cycle_parent[min_cycle_b]
    res.appendleft(min_cycle_a)
    while res:
        res_l.append(res.popleft())
    return res_l

### sprawdzenie czy dla grafu G (o ktorym zakladamy, ze ma cykl Eulera
### funkcja zwraca prawidłowy wynik
  
G = [[-1, 2,-1,-1, 1],
     [ 2,-1, 4, 1,-1],
     [-1, 4,-1, 5,-1],
     [-1, 1, 5,-1, 3],
     [ 1,-1,-1, 3,-1]]

LEN = 7


GG = deepcopy( G )
cycle = min_cycle( GG )

print("Cykl :", cycle)


if cycle == []:
  print("Błąd (1): Spodziewano się cyklu!")
  exit(0)

L = 0
u = cycle[0]
for v in cycle[1:]+[u]:
  if G[u][v] == -1:
    print("Błąd (2): To nie cykl! Brak krawędzi ", (u,v))
    exit(0)
  L += G[u][v]
  u = v

print("Oczekiwana długość :", LEN)
print("Uzyskana długość   :", L)

if L != LEN:
  print("Błąd (3): Niezgodna długość")
else:
  print("OK")

