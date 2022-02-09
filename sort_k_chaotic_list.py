class Node():
    def __init__(self):
        self.val = None
        self.next = None


def make_list_from_tab(tab):
    n = len(tab)
    res = Node()
    res.val = tab[0]
    e = res
    for i in range(1, n):
        x = Node()
        x.val = tab[i]
        e.next = x
        e = e.next

    return res


def print_list(L):
    while L != None:
        print(L.val, end=" -> ")
        L = L.next
    print("\n")

def left(i):
    return (2 * i) + 1


def right(i):
    return (2 * i) + 2


def parent(i):
    return (i - 1) // 2


def heapify(tab, n, i):
    while i < n:
        minimum = i
        l = left(i)
        r = right(i)
        if l < n and tab[l].val < tab[minimum].val: minimum = l
        if r < n and tab[r].val < tab[minimum].val: minimum = r

        if minimum == i:
            return
        else:
            tab[i], tab[minimum] = tab[minimum], tab[i]
            i = minimum


def makeheap(tab, n):
    for i in range(parent(n - 1), -1, -1):
        heapify(tab, n, i)


def add_to_heap(tab, el):
    tab.append(el)
    n = len(tab)
    x = n - 1
    p = parent(x)
    while p >= 0 and tab[p].val > tab[x].val:
        tab[p], tab[x] = tab[x], tab[p]
        x = p
        p = parent(x)


def remove_and_return_top_from_heap(tab,n):
    tab[0], tab[n - 1] = tab[n - 1], tab[0]
    heapify(tab, n - 1, 0)
    return tab.pop()


def SortH(p, k):
    k = k+1
    res_guard = Node()
    res_end = res_guard

    heap = [0] * k
    heap_len = 0

    ptr = p
    for i in range(k):
        if ptr == None:
            break
        heap[i] = ptr
        heap_len += 1
        ptr = ptr.next


    makeheap(heap,heap_len)

    while ptr != None:
        res_end.next = remove_and_return_top_from_heap(heap, heap_len)
        res_end = res_end.next
        add_to_heap(heap, ptr)
        ptr = ptr.next

    while heap_len != 0:
        res_end.next = remove_and_return_top_from_heap(heap, heap_len)
        heap_len -= 1
        res_end = res_end.next

    res_end.next = None
    return res_guard.next

tab = [1, 3, 0, 4, 2, 6, 5, 7]
L = make_list_from_tab(tab)

res = SortH(L, 2)
print_list(res)




