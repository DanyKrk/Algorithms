def quicksort(tab):
    def partition(tab, b, e):
        x = tab[e]
        i = b - 1
        for j in range(b, e):
            if tab[j] <= x:
                i += 1
                tab[i], tab[j] = tab[j], tab[i]
        tab[i + 1], tab[e] = tab[e], tab[i + 1]
        return i + 1

    def quicksort_int(tab, b, e):
        while b < e:
            q = partition(tab, b, e)
            if q - b < e - q:
                quicksort_int(tab, b, q - 1)
                b = q + 1
            else:
                quicksort_int(tab, q + 1, e)
                e = q - 1

    n = len(tab)
    quicksort_int(tab, 0, n - 1)


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


def quicksort_iter(tab):  # quicksort bez rekurencji
    def partition(tab, b, e):
        x = tab[e]
        i = b - 1
        for j in range(b, e):
            if tab[j] <= x:
                i += 1
                tab[i], tab[j] = tab[j], tab[i]
        tab[i + 1], tab[e] = tab[e], tab[i + 1]
        return i + 1

    n = len(tab)
    stack = []
    stack.append((0, n - 1))

    while len(stack) != 0:
        b, e = stack.pop()
        if b >= e: continue

        q = partition(tab, b, e)
        if q - b < e - q:
            stack.append((q + 1, e))
            stack.append((b, q - 1))
        else:
            stack.append((b, q - 1))
            stack.append((q + 1, e))




A = [5,43,23,423,4,234,23,5]
print("przed sortowaniem: ", A)
quicksort_iter(A)
print("po sortowaniu: ", A)
