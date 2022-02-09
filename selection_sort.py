def selection_sort(tab):
    n = len(tab)
    for i in range(n):
        min = i
        for j in range(i,n):
            if tab[j]<tab[min]: min = j
        tab[i], tab[min] = tab[min], tab[i]

