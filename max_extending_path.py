#Daniel Krzykawski
#Algorytm to zmodyfikowany algorytm Dijkstry, w którym wyciągamy z kolejki wierzchołki do których możemy dojść z największą przepustowością
#Złożoność jak w Dijkstrze O(E*logE) bo ilość elementów w kolejce może być rzędu E, a ilość operacji na kolejce może być też rzędu E.

from copy import deepcopy
from queue import PriorityQueue
from math import inf

def max_extending_path( G, s, t ):
  n = len(G)
  visited = [False] * n
  parent = [-1] * n
  P = PriorityQueue()
  P.put((-inf,s,s)) #na kolejke wrzucam krotki (z jaką ilośćią pasażerów wchodzę do wierzchołka, z którego wierzchołka, do którego wierzchołka)
                    # ilość pasażerów wrzucam jako liczbę ujemną, żeby PriorityQueue wyciągało najpierw maksymalne ilości pasażerów
  while not P.empty():
    u = P.get()
    u_id = u[2]
    u_passengers = -u[0] #zamieniam liczbe pasażerów z powrotem na liczbę dodatnią
    u_parent = u[1]

    if visited[u_id]: continue

    parent[u_id] = u_parent
    visited[u_id] = True

    if u_id == t: break

    for v in G[u_id]:
      v_id = v[0]
      v_volume = v[1]

      if visited[v_id]: continue

      P.put((-min(v_volume,u_passengers), u_id, v_id))

  def make_res(parent,t, res):
    if parent[t] == -1: #jeżeli nie ma rozwiązania, zwracam pustą listę
      res = [None]
      return
    if parent[t] != t:
      make_res(parent, parent[t], res)
    res.append(t)

  res = []
  make_res(parent,t,res)

  return res

  
### sprawdzenie czy dla grafu G (o ktorym zakladamy, ze ma cykl Eulera
### funkcja zwraca prawidłowy wynik

G = [[(1,4), (2,3)], # 0
     [(3,2)], # 1
     [(3,5)], # 2
     []] # 3


s = 0
t = 3
C = 3


GG = deepcopy( G )
path = max_extending_path( GG, s, t )

print("Sciezka :", path)


if path == []:
  print("Błąd (1): Spodziewano się ścieżki!")
  exit(0)

if path[0] != s or path[-1] != t:
  print("Błąd (2): Zły początek lub koniec!")
  exit(0)


capacity = float("inf")
u = path[0]

for v in path[1:]:
  connected = False
  for (x,c) in G[u]:
    if x == v:
      capacity = min(capacity, c)
      connected = True
  if not connected:
    print("Błąd (3): Brak krawędzi ", (u,v))
    exit(0)
  u = v

print("Oczekiwana pojemność :", C)
print("Uzyskana pojemność   :", capacity)

if C != capacity:
  print("Błąd (4): Niezgodna pojemność")
else:
  print("OK")

