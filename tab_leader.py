def select(tab,b,e,n):
    def partition(tab,b,e):
        x = tab[e]
        i = b-1
        for j in range(b,e):
            if tab[j]<=x:
                i+=1
                tab[i],tab[j]=tab[j],tab[i]
        tab[i+1],tab[e] = tab[e], tab[i+1]
        return i+1

    if b == e: return tab[b]
    q = partition(tab,b,e)
    if q == n: return tab[q]
    if n<q: return select(tab,b,q-1,n)
    else: return select(tab,q+1,e,n)

def tab_leader(tab):
    n = len(tab)
    candidate = select(tab,0,n-1,(n-1)//2)
    counter = 1
    i = ((n-1)//2)-1
    while i >= 0 and tab[i] == candidate:
        counter+=1
        i-=1
    i =((n-1)//2)+1
    while i<n and tab[i] == candidate:
        counter += 1
        i += 1
    if counter > n//2:
        return candidate
    else:
        return "no leader"

A = [7,2,7,7,2,2,2,2,2,2,3,5]
print(tab_leader(A))