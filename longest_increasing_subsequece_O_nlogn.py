from math import inf
def lcs(T):
    n = len(T)
    decks_top = [-1] * n
    decks_top[0] = T[0]
    decks_counter = 1
    for i in range(1,n):
        for j in range(decks_counter+2):
            if j == decks_counter + 1:
                decks_counter += 1
                decks_top[decks_counter-1] = T[i]
                break
            elif decks_top[j]>=T[i]:
                decks_top[j] = T[i]
                break
    return decks_counter, decks_top

T = [5,4,3,2,7,1,8]
print(lcs(T))
#zeby wyp