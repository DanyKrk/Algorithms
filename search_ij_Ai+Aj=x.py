def find_i_j(tab, x):
    n = len(tab)
    i = 0
    j = n - 1
    sum = tab[i] + tab[j]
    while j - i>1 and sum != x:
        if sum < x:
            i += 1
        else:
            j -= 1
        sum = tab[i]+tab[j]
    if sum == x:
        return i,j
    return "No result"

tab = [-6,-5,-3,0,5,9,35,45]
print(find_i_j(tab,5))