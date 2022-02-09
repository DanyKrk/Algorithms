def partition(tab, p, r):
  pivot = tab[p]
  i = p - 1
  j = r + 1

  while (True):
    i += 1
    while(tab[i] < pivot):
      i += 1

    j -= 1
    while(tab[j] > pivot):
      j -= 1

    if i >= j:
      return j

    tab[i], tab[j] = tab[j], tab[i]


def qs_iter(tab):
  stack = []
  stack.append((0, len(tab)-1))
  while len(stack)>0:
    p,r = stack.pop()
    if p < r:
      q = partition(tab, p, r)
      stack.append((p,q))
      stack.append((q+1,r))


A = [5,3,2,8,2,3,9,0]
#A = [5]
qs_iter(A)
print(A)