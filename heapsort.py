def left(i):
    return (2 * i) + 1


def right(i):
    return (2 * i) + 2


def parent(i):
    return (i - 1) // 2


def heapify(tab, n, i):
    while i < n:
        maximum = i
        l = left(i)
        r = right(i)
        if l < n and tab[l] > tab[maximum]: maximum = l
        if r < n and tab[r] > tab[maximum]: maximum = r

        if maximum == i:
            return
        else:
            tab[i], tab[maximum] = tab[maximum], tab[i]
            i = maximum

def makeheap(tab, n):
       for i in range(parent(n - 1), -1, -1):
           heapify(tab, n, i)


def add_to_heap(tab,el):
    tab.append(el)
    n = len(tab)
    x = n-1
    p = parent(x)
    while p>=0 and tab[p]<tab[x]:
        tab[p], tab[x] = tab[x], tab[p]
        x = p
        p = parent(x)

def remove_and_return_top_from_heap(tab):
    n = len(tab)
    tab[0], tab[n-1] = tab[n-1], tab[0]
    heapify(tab,n-1,0)
    return tab.pop()


def heapsort(tab):
    n = len(tab)

    makeheap(tab,n)

    for i in range(n-1,-1,-1):
        tab[0],tab[i] = tab[i], tab[0]
        heapify(tab,i,0)


tab = [2,4,23,5,2,62,236,324,6,2363]
n = len(tab)
makeheap(tab, n)
add_to_heap(tab,400)
print(tab)
print(remove_and_return_top_from_heap(tab))
print(tab)