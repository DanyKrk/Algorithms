def insertion_sort(tab):
    n = len(tab)
    for i in range(1,n):
        x = tab[i]
        j = i-1
        while j>=0 and tab[j] > x:
            tab[j+1] = tab[j]
            j-=1
        tab[j+1] = x

def bucket_sort(tab, b, e): # b -początek zakresu z którego dane, e - koniec tego zakresu
    n = len(tab)
    buckets = [[] for i in range(n)]
    bucket_size = (e-b)/n
    for i in range(n):
        buckets[int((tab[i]-b)/bucket_size)].append(tab[i])
    for i in range(n):
        insertion_sort(buckets[i])

    i = 0
    for A in buckets:
        for x in A:
            tab[i] = x
            i+=1

tab = [0.64,0.36,0.3453,0.87,0.1,0.2,0.4,0.9,0.7,0.5,0]
bucket_sort(tab,0.0,1.0)
print(tab)