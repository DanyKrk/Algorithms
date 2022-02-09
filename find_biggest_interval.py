def quicksort_with_function(tab, f):  # wersja z funcją po czym sortować
    def partition(tab, b, e, f):
        x = f(tab[e])
        i = b - 1
        for j in range(b, e):
            if f(tab[j]) <= x:
                i += 1
                tab[i], tab[j] = tab[j], tab[i]
        tab[i + 1], tab[e] = tab[e], tab[i + 1]
        return i + 1

    def quicksort_int(tab, b, e, f):
        while b < e:
            q = partition(tab, b, e, f)
            if q - b < e - q:
                quicksort_int(tab, b, q - 1, f)
                b = q + 1
            else:
                quicksort_int(tab, q + 1, e, f)
                e = q - 1

    n = len(tab)
    quicksort_int(tab, 0, n - 1, f)


def bin_search_with_function(tab, x, f):  # wersja z funkcją, po czym patrzec
    n = len(tab)

    def bin_search_int(tab, b, e, x, f):
        if b > e:
            return None
        mid = b + ((e - b) // 2)
        if f(tab[mid]) == x:  # tu dodatkowo sprawdzam jeszcze, czy to najmiejszy indeks, który ma tą wartość
            check = bin_search_int(tab, b, mid - 1, x, f)
            if check != None: return check
            return mid
        elif x < f(tab[mid]):
            return bin_search_int(tab, b, mid - 1, x, f)
        else:
            return bin_search_int(tab, mid + 1, e, x, f)

    return bin_search_int(tab, 0, n - 1, x, f)


def find_biggest_interval(tab):
    n = len(tab)
    A = []  # tablica z punktami
    F = [0 for i in range(2 * n)]  # ile przedziałów zaczęło się przed lub na i
    G = [0 for i in range(2 * n)]  # ile przedziałów skończyło się przed lub na i

    for i in tab:
        A.append(("b", i[0], i[1]))
        A.append(("e", i[1], i[0]))

    quicksort_with_function(A, lambda x: x[1])

    if A[0][0] == "b":
        F[0] = 1
    else:
        G[0] = 1

    for i in range(1, 2 * n):
        G[i] = G[i - 1]
        F[i] = F[i - 1]
        if A[i][0] == "b":
            F[i] += 1
        else:
            G[i] += 1

    max = 0
    max_b = 0
    max_e = 0
    for i in range((2 * n) - 1, 0, -1):
        if A[i][0] == "e":
            j = bin_search_with_function(A, ("b", A[i][2]), lambda x: (x[0], x[1]))
            if G[i] - F[i] >= max:
                max = G[i] - F[i]
                max_e = i
                max_b = j

    return (A[j][1], A[i][1])


# A = [(1,3),(2,6),(1,3),(3,4)]
# print(find_biggest_interval(A))
A = [('b', 1, 3), ('e', 3, 1), ('b', 2, 6), ('e', 6, 2), ('b', 1, 3), ('e', 3, 1), ('b', 3, 4), ('e', 4, 3)]

quicksort_with_function(A, lambda x: x[1])
x = bin_search_with_function(A,2,lambda x: x[1])
print(x)
print(A)
