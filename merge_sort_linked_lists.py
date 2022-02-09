class Node():
    def __init__(self):
        self.val = None
        self.next = None


def print_list(a):
    if a == None:
        print("None")
        return
    print(a.val, " - ", end="")
    print_list(a.next)


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


def merge_lists(a, b):
    if a == None or b == None: return

    if a.val > b.val:  # c - głowa wyniku, e - ostatni node wyniku
        c = b
        b = b.next
    else:
        c = a
        a = a.next
    e = c

    while True:
        if a == None:
            e.next = b
            return c
        if b == None:
            e.next = a
            return c

        if a.val < b.val:
            e.next = a
            e = e.next
            a = a.next
        else:
            e.next = b
            e = e.next
            b = b.next


def merge_sort_linked_list(L):  # sortuje łącząc kolejne serie naturalne parami
    if L == None: return None

    guard = Node()
    guard.val = 'G'
    guard.next = L
    L = guard

    e = guard  # wskaznik do ktorego bede przylepial zmergowane serie
    b1 = None
    e1 = None   #początki i konce odpowiednio 1 serii naturalnej i 2 serii naturalnej
    b2 = None
    e2 = None
    b = None #wskaznik na początek ogona (to co trzeba dopiąc do zmergowanych serii)

    scout = guard.next.next
    b1 = e1 = guard.next
    while True:
        if scout == None:
            if b1 == guard.next:# lista jest posortowana
                return b1
            else:               #zaczynam od początku listy
                b1 = e1 = guard.next
                scout = guard.next.next
                e = guard

        if e1.val > scout.val: #e1 jest osatnim elementem 1 serii naturalnej
            b2 = e2 = scout
            scout = scout.next
            while True:
                if scout == None or e2.val > scout.val: #dochodze do konca 2 serii naturalnej
                    b = scout
                    e1.next = None #odpinam do mergowania
                    e2.next = None
                    c = merge_lists(b1,b2)
                    e.next = c       #dopinam zmergowane serie
                    if e1.val >e2.val: #do konca zmergowanego dopinam ogon i ustawiam nowy e(przystań)
                        e1.next = b
                        e = e1
                    else:
                        e2.next = b
                        e = e2
                    b1 = b              #ustawiam nowe b1 i e1 (jak moge to scout tez) do nastepnego wyszukiwania (reszta sie ustawia pod koniec zewnetrznej petli po break)
                    break
                e2 = scout
                scout = scout.next

        e1 = scout
        if scout != None: scout = scout.next



tab1 = [1, 3, 5, 7]
tab2 = [2, 4, 6, 8, 10]
tab3 = [5,3,7,4,5,6,2,1,8,5,345,234,53,6,45,72,57,52,47,346,8,647,245,76,256,56]



d = make_list_from_tab(tab3)
print_list(d)
d = merge_sort_linked_list(d)
print_list(d)
