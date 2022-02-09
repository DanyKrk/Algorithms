def count_sort(tab, k):
    n = len(tab)
    A = [0 for i in range(k)]
    B = [0 for i in range(n)]
    for x in tab:
        A[x]+=1
    for i in range(1,k):
        A[i] += A[i-1]

    for i in range(n-1,-1,-1):
        A[tab[i]]-=1
        B[A[tab[i]]] = tab[i]

    for i in range(n):
        tab[i] = B[i]


tab = [3,5,7,3,4,5,4,2,9,0,3,8,8,8,8,5,4,3,7,6,4,5,3,4,7,3,3,1,3,1,2,5,5]
count_sort(tab,10)
print(tab)