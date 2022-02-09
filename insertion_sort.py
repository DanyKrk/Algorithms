def insertion_sort(tab):
    n = len(tab)
    for i in range(1,n):
        x = tab[i]
        j = i-1
        while j>=0 and tab[j] > x:
            tab[j+1] = tab[j]
            j-=1
        tab[j+1] = x

tab = [5,2,7,3,7,8,3,4,73,2,64,4357,562,6,4253,7,26,347,6,27,3273,24,36,356,62,6,2,345,6,437,4,7,467,36,73,47,346,7]

insertion_sort(tab)
print(tab)