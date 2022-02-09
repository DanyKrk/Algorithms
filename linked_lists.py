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


def add_node_to_sorted_list(A, el_node):
    if A == None:
        return el_node

    q = None
    p = A
    while p != None and p.val < el_node.val:
        q = p
        p = p.next
    if p != A:
        q.next = el_node
        el_node.next = p
    else:
        el_node.next = p
        A = el_node
    return A


def merge_sorted_lists(A, B): #zwraca wskaźnik na początek
    C = Node()
    C_end = C
    while A != None and B != None:
        if (A.val < B.val):
            C_end.next = A
            A = A.next
        else:
            C_end.next = B
            B = B.next
        C_end = C_end.next
    if A == None:
        C_end.next = B
    else:
        C_end.next = A
    return C.next

def merge_sorted_lists_2(A, B): #zwraza wskaźnik na koniec i początek
    C = Node()
    C_end = C
    while A != None and B != None:
        if (A.val < B.val):
            C_end.next = A
            A = A.next
        else:
            C_end.next = B
            B = B.next
        C_end = C_end.next
    if A == None:
        C_end.next = B
        end = B
        while end.next != None:
            end = end.next
    else:
        C_end.next = A
        end = A
        while end.next != None:
            end = end.next
    return C.next, end



