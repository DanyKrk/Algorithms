def min_max(tab):
    n = len(tab)
    maximum = tab[n-1]
    minimum = tab[n-1]
    for i in range(1,n,2):
        if(tab[i-1]>tab[i]):
            tab[i-1], tab[i] = tab[i], tab[i-1]
        if tab[i-1]<minimum:
            minimum = tab[i-1]
        if tab[i] > maximum:
            maximum = tab[i]
    return (minimum, maximum)




A = [3,94,2]

print(min_max(A))