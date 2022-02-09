def merge(T, help_tab, b1, e1, b2, e2): #funckja scali zakresy b1-e1 i b2-e2 (włącznie) i wstawi w oryginalnej tablicy zaczynając od b1 #STABILNIE
    if b1 == b2 == e1 == e2: return
    b = b1
    n = e1 - b1 + e2 - b2 + 2
    for i in range(n):
        if b1 > e1:
            for j in range(b2, e2 + 1):
                help_tab[i] = T[j]
                i += 1
            break
        if b2 > e2:
            for j in range(b1, e1 + 1):
                help_tab[i] = T[j]
                i += 1
            break
        if T[b1] > T[b2]:
            help_tab[i] = T[b2]
            b2 += 1
        else:
            help_tab[i] = T[b1]
            b1 += 1

    for i in range(n):
        T[b] = help_tab[i]
        b += 1


def merge_sort(T):
    def merge_sort_recursion(T, help_tab, b, e):
        if b == e: return
        n = e-b + 1
        b1 = b
        e1 = b1 + int(n/2)-1
        b2 = e1+1
        e2 = e
        merge_sort_recursion(T, help_tab, b1, e1)
        merge_sort_recursion(T, help_tab, b2, e2)
        merge(T, help_tab, b1, e1, b2, e2)

    n = len(T)
    help_tab = [0]*n
    merge_sort_recursion(T, help_tab, 0, n-1)

T = [7,3,5,7,100,1003,2,4,6,6,8, 9,11,55]
n = len(T)
help_tab = [0]*n
merge(T, help_tab, 0,0,6,7)
print(T)
merge_sort(T)
print(T)


