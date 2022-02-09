
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



def bin_search_with_function(tab,x,f): # połówkowe wyszukiwanie indeksu kubełka do którego ma należeć x (w tab mamy początki zakresów)
    n = len(tab)
    def bin_search_int(tab,b,e,x,f):
        if b>e:
            return None
        mid = b+((e-b)//2)
        if f(tab[mid]) <= x and (mid + 1 == n or f(tab[mid+1]) > x): # tu dodatkowo sprawdzam jeszcze, czy to najmiejszy indeks, który ma tą wartość
            return mid
        elif x < f(tab[mid]): return bin_search_int(tab,b,mid-1,x,f)
        else: return bin_search_int(tab,mid+1,e,x,f)

    return bin_search_int(tab,0,n-1,x,f)

def insertion_sort(tab):
    n = len(tab)
    for i in range(1,n):
        x = tab[i]
        j = i-1
        while j>=0 and tab[j] > x:
            tab[j+1] = tab[j]
            j-=1
        tab[j+1] = x

def bucket_sort_omit_0(tab, b, e): # b -początek zakresu z którego dane, e - koniec tego zakresu
    n = len(tab) - 1
    buckets = [[] for i in range(n)]
    bucket_size = (e-b)/n
    for i in range(1,n):
        buckets[int((tab[i]-b)/bucket_size)].append(tab[i])
    for i in range(1,n):
        insertion_sort(buckets[i])

    i = 1
    for A in buckets:
        for x in A:
            tab[i] = x
            i+=1

def SortTab(T,P): #T - tablica do posortowania, P - tablica opisująca przedziały - krotki (an,bn, cn) - przedział[an,bn], wybierany z prawdopodobienstwem cn
    n = len(P)
    sections = [[0] for i in range(2*n)]

    for i in range(n):
        sections[2*i][0] = P[i][0]
        sections[2*i+1][0] = P[i][1]

    print(sections)
    quicksort_with_function(sections,lambda x:x[0])

    for i in range(len(T)):
        sections[bin_search_with_function(sections,T[i],lambda x:x[0])].append(0)



    for i in range(len(sections)-1):
        bucket_sort_omit_0(sections[i],sections[i][0],sections[i+1][0])

    i = 0
    for A in sections:
        for x in range(1,len(A)):
            T[i] = x
            i+=1

P = [(1,5, 0.75) , (4,8, 0.25)]
T = [6.1, 1.2, 1.5, 3.5, 4.5, 2.5, 3.9, 7.8]
SortTab(T,P)
print(T)








