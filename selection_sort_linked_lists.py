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


def selection_sort(L): #raczej stabilny
    if L == None: return

    #dla wygody dodaje wartownika
    guard = Node()
    guard.next = L

    #sprawiam, aby największy element listy był na jej początku
    i = L
    biggest_val = L.val
    el_before_biggest_val = guard
    while i.next != None:
        if i.next.val > biggest_val:
            biggest_val = i.next.val
            el_before_biggest_val = i
        i = i.next

    if el_before_biggest_val != guard:
        guard.next = el_before_biggest_val.next
        el_before_biggest_val.next = el_before_biggest_val.next.next
        guard.next.next = L

    #zaznaczam ostatni element wyniku (nie będzie sie zmieniał, bo jest  największym el)
    end_of_res = guard.next

    #dopóki moge dopinam na początek największe elementy z źródła
    while end_of_res.next!= None:
        biggest_val = end_of_res.next.val
        el_before_biggest_val = end_of_res

        i = end_of_res.next
        while i.next != None:
            if i.next.val >= biggest_val:
                biggest_val = i.next.val
                el_before_biggest_val = i
            i = i.next

        beginning_of_old_res = guard.next
        el_after_biggest_val = el_before_biggest_val.next.next
        guard.next = el_before_biggest_val.next
        el_before_biggest_val.next.next = beginning_of_old_res
        el_before_biggest_val.next = el_after_biggest_val

    return guard.next

L = tab_to_list([9,5,6,2,6,25,7,457,2,5,3,6,457,347,25,6,32,6,2457,254,72,56,3,6,25,7,2456,235,6,3])
L = selection_sort(L)
print_list(L)

