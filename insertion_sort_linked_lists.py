class Node():
    def __init__(self):
        self.val = None
        self.next = None


def print_list(L):
    while L != None:
        print(L.val, end=" -> ")
        L = L.next
    print("\n")

def add_el_to_list_front(A,el):
    x = Node()
    x.val = el
    x.next = A
    return x

def add_node_to_list_front(A,x):
    x.next = A
    return x

def tab_to_list(tab):
    n = len(tab)
    A = None
    for i in range(n-1,-1,-1):
        x = Node()
        x.val = tab[i]
        A = add_node_to_list_front(A,x)
    return A

def insertion_sort_LL(L): #niedokonczone
    if L == None: return

    i = L #wskaznik na node przed tym ktory rozważamy
    while i.next != None:
        if i.next.val < L.val:
            s = i.next.next
            i.next.next = L
            L = i.next
            i.next = s
            continue

        j = L #wskaznik na element po którym mamy wstawic i.next
        while j.next != i.next and j.next.val<=i.next.val:  j = j.next

        if j.next == i.next: #jak i jest na swoim miejscu
            i = i.next
            continue

        big_fella = j.next
        si = i.next.next
        sj = j.next.next
        j.next = i.next
        j.next.next = sj
        i.next = big_fella
        i.next.next = si


