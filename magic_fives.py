from random import randint, shuffle, seed

def selection_sort(A,p,r):
  for i in range(p,r):
    mn = i
    for j in range(i+1,r+1):
      if A[j]<A[mn]: mn = j
    A[i], A[mn] = A[mn], A[i]



def magic_fives(A, p,r):
  n = r-p + 1
  if n%5 == 0:   # wyznaczam ilość piątek
    fives = n//5
  else:
    fives = n//5 + 1

  if fives == 1: # warunek wyjścia - zwracam medianę median
    selection_sort(A,p,r)
    A[p+((r-p)//2)], A[p] = A[p], A[p+((r-p)//2)] #przestawiam medianę na początek, żeby w partition znać jej indeks
    return A[p]

  i = p
  while i < (p+((fives-1)*5)):  # wyznaczam mediany w na pewno pełnych piątkach
    selection_sort(A,i,i+4)
    A[i+2], A[p+((i-p)//5)] = A[p+((i-p)//5)], A[i+2]  # mediany przestawiam na początek sprawdzanego zakresu, żeby móc potem łatwo rekurencyjnie wyznaczyć ich medianę
    i += 5

  selection_sort(A,i,r) #ostatnia piątka
  A[p+fives-1], A[i + ((r-i+1)//2)] = A[i + ((r-i+1)//2)], A[p+fives-1]

  return magic_fives(A, p, p+fives-1)

def partition(A, p, r):
  if p == r: return p

  x = magic_fives(A,p,r)

  A[p], A[r] = A[r], A[p] #przestawiam medianę na koniec, żeby móc ją potem przestawić na indeks q, żeby pominąć ją przy kolejnych wywołaniach select_int

  i = p-1
  for j in range(p,r,1):
    if A[j]<x:
      i += 1
      A[i], A[j] = A[j], A[i]

  A[i+1], A[r] = A[r], A[i+1] #przestawiam medianę na indeks q (i+1)
  return i+1



def select_int(A, p, r, k): #algorytm select interior - konieczny ze względu na argumenty
  if p == r: return A[p]

  q = partition(A, p, r)

  if q == k: return A[q]

  if k<q:
    return select_int(A, p, q-1, k)
  else:
    return select_int(A, q+1, r, k)


def linearselect( A, k ):
  n = len(A)
  return select_int(A,0,n-1,k)


seed(42)

n = 11
for i in range(n):
  A = list(range(n))
  shuffle(A)
  print(A)
  x = linearselect(A, i)
  if x != i:
    print("Blad podczas wyszukiwania liczby", i)
    exit(0)

print("OK")

