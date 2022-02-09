class Node:
    def __init__(self):
        self.next = None
        self.value = None


def partition(b, e):
    sm_b = Node()
    sm_b.value = wartownik
    sm_e = sm_b

    eq_b = Node()
    eq_b.value = wartownik
    eq_b.next = b
    eq_e = b
    b = b.next


    gt_b = Node()
    gt_b.value = wartownik
    gt_e = gt_b

    while True:
        if b.value < eq_e.value:
            sm_e.next = b
            sm_e = sm_e.next
        if b.value = eq_e.value:
            eq_e.next = b
            eq_e = eq_e.next
        if b.value > eq_e.value:
            gt_e.next = b
            gt_e = gt_e.next

        if b == e: break
        b = b.next


    sm_b = sm_b.next
    eq_b = eq_b.next
    qt_b = gt_b.next
    if sm_e.value == wartownik: sm_e = None
    if gt_e.value == wartownik: gt_e = None

    return sm_b, sm_e, eq_b, eq_e, gt_b, gt_e




def qsort_2arg(b, e):
    if b == e:
        return b, e
    else:
        sm_b, sm_e, eq_b, eq_e, gt_b, gt_e = partition(b, e)
        if sm_b == None:
            sm_b = eq_b
        else:
            b, sm_e = qsort_2arg(b, sm_e)
            sm_e.next = eq_b
        if gt_b == None:
            gt_e = eq_e
        else:
            gt_b, e = qsort_2arg(gt_b, e)
            eq_e.next = gt_b

        return (b, e)


def qsort(b):
    if b == None or b.next == None: return b

    e = b
    while e.next != None:
        e = e.next

    b, e = qsort_2arg(b, e)
    return b

