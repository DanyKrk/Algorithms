def reverse_linked_list(L):
    if L == None:
        return L
    r = None
    q = L
    p = L.next
    while p != None:
        q.next = r
        r = q
        q = p
        p = p.next
    q.next = r
    return q