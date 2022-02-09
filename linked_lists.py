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


A = None
for i in range(0, 10, 2):
    x = Node()
    x.val = i
    A = add_to_sorted(A, x)
