def select_zle(tab,b,e,n):
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


    # b = 0
    # e = n-1
    # while b<e:
    #     q = partition(tab,b,e)
    #     if n == q:
    #         return tab[q]
    #     elif n<q:
    #         b = q+1
    #     else: e = q-1
    # return tab[b]

def select(A,p,r,k):
    def partition(tab,b,e):
        x = tab[e]
        i = b-1
        for j in range(b,e):
            if tab[j]<=x:
                i+=1
                tab[i],tab[j]=tab[j],tab[i]
        tab[i+1],tab[e] = tab[e], tab[i+1]
        return i+1

    if p == r:
        return A[p]
    q = partition(A,p,r)
    if q == k:
        return A[q]
    elif k<q:
        return select(A,p,q-1,k)
    else:
        return select(A,q+1,r,k)



tab = [5,3,26,72,45,4,54,645,64]
n = len(tab)
print(select(tab,0,n-1,-1))