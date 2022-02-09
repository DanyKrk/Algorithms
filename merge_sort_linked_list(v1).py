class Node():
    def __init__(self):
        self.val = None
        self.next = None


def merge_sorted_lists(A, B):
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


def print_list(L):
    while L != None:
        print(L.val, end=" -> ")
        L = L.next
    print("\n")


def add_el_to_list_front(A, el):
    x = Node()
    x.val = el
    x.next = A
    return x


def add_node_to_list_front(A, x):
    x.next = A
    return x


def tab_to_list(tab):
    n = len(tab)
    A = None
    for i in range(n - 1, -1, -1):
        x = Node()
        x.val = tab[i]
        A = add_node_to_list_front(A, x)
    return A


def cat_list(A):
    if A == None: return None

    while A.next != None and A.next.val >= A.val:
        A = A.next
    B = A.next
    A.next = None
    return B

def merge_sort_linked_list(A):
    B = cat_list(A)
    if B == None:
        return A
    C = cat_list(B)
    A,end = merge_sorted_lists(A, B)
    while C!= None:
        D = cat_list(C)
        E = cat_list(D)
        C ,end1 = merge_sorted_lists(C, D)
        end.next = C
        end = end1
        C = E
    A = merge_sort_linked_list(A)
    return A

def merge_sort_linked_list_iter(A):
    while True:
        NH = None
        NT = None
        while True:
            B = A
            A = cat_list(A)
            if A == None and NT == None: return B
            if A == None:
                NT.next = B
                break

            C = A
            A = cat_list(A)
            if NH == None:
                NH,NT = merge_sorted_lists(B,C)
            else:
                NT.next,NT = merge_sorted_lists(B,C)

        A = NH










tab = [2,35,9,10]
A = tab_to_list(tab)
print_list(A)
print("Sortowanie: ")

A = merge_sort_linked_list_iter(A)
print_list(A)

