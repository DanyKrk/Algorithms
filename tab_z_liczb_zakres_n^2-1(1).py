def count_sort(tab, f):
    n = len(tab)
    A = [0 for i in range(n)]
    B = [0 for i in range(n)]

    for i in tab:
        A[f(i)] += 1
    for i in range(1, n):
        A[i] += A[i - 1]
    for i in range(n - 1, -1, -1):
        A[f(tab[i])] -= 1
        B[A[f(tab[i])]] = tab[i]
    for i in range(n):
        tab[i] = B[i]


def radix_sort(tab):
    n = len(tab)
    count_sort(tab, lambda x: x % n)
    count_sort(tab, lambda x: x // n)


tab = [5, 3, 6, 1, 5, 54,24,7,5,2,3,6,8,5,9,2,234,53,2,78,253,4,4]

radix_sort(tab)

print(tab)
