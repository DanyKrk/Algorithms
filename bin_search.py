def bin_search(tab,x):
    n = len(tab)
    def bin_search_int(tab,b,e,x):
        if b>e:
            return "nima"
        mid = b+((e-b)//2)
        if tab[mid] == x: # tu dodatkowo sprawdzam jeszcze, czy to najmiejszy indeks, który ma tą wartość
            check = bin_search_int(tab,b,mid-1,x)
            if check != None: return check
            return mid
        elif x < tab[mid]: return bin_search_int(tab,b,mid-1,x)
        else: return bin_search_int(tab,mid+1,e,x)

    return bin_search_int(tab,0,n-1,x)

tab = [1,3,5]
bin_search(tab,4)