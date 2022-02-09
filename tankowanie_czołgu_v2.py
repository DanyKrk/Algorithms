from math import inf

def zad_a(L, S, P, T):
    n = len(S)
    curr_station = -1
    curr_pos = 0
    curr_vol = L
    refuelings_counter = 0
    while (True):
        if T - curr_pos <= curr_vol: return refuelings_counter  # jak T jest w moim zasięgu - idę tam
        if curr_station == n - 1: return "nie da sie dojechac do T"  # jestem na ostatniej stacji i nie moglem dojechac do T

        i = curr_station + 1
        while i < n and S[i] - curr_pos <= curr_vol: i += 1  # T nie jest w zasięgu - wyszukuje najdalszą możliwą stację
        i -= 1
        curr_pos = S[i]  # idę na tą stację
        curr_station = i
        refuelings_counter += 1


def zad_b1(L, S, P, T):
    n = len(S)
    spent = 0
    curr_pos_ind = -1
    curr_vol = L

    min_price = inf
    min_price_ind = -1
    i = 0
    while i < n and S[i] <= L:  # przeglądam stacje, do których mogę dojechać
        if P[i] <= min_price:
            min_price = P[i]
            min_price_ind = i
        i += 1
    curr_vol -= S[min_price_ind]  # jadę do najtańszej stacji początkowej
    curr_pos_ind = min_price_ind

    while S[curr_pos_ind] != T:  # dopóki nie znajde sie na stacji końcowej (zakładam, że T jest ostatnią stacją - wiem że zostanie wybrana przez aglorytm bo ma koszt 0)
        i = curr_pos_ind + 1
        min_price = inf
        while i < n and S[i] - S[curr_pos_ind] <= L:  # przegądam stacje do których moge dojechac i szukam najtańszej
            if P[i] <= min_price:
                min_price = P[i]
                min_price_ind = i
            i += 1
        dist_to_min_price = S[min_price_ind] - S[curr_pos_ind]

        if min_price <= P[curr_pos_ind]:  # kiedy widze stacje nie droższą od obecnej - ewentualnie dodatnkowuję, tak żeby dojechać "na styk"
            if dist_to_min_price <= curr_vol:  # jak nie musze dotankować
                curr_vol -= dist_to_min_price
                curr_pos_ind = min_price_ind
                continue
            else:  # jak muszę dotankować, żeby dojechać
                spent += P[curr_pos_ind] * (dist_to_min_price - curr_vol)
                curr_pos_ind = min_price_ind
                curr_vol = 0
                continue
        else:  # kiedy widzę tylko droższe stacje
            spent += (L - curr_vol) * P[curr_pos_ind]  # tankuje do pełna i jade do najtańszej stacji
            curr_vol = L - dist_to_min_price
            curr_pos_ind = min_price_ind

    return spent


def zad_b2(L, S, P, T):
    n = len(S)
    F = [inf for i in range(n)]  # F[i] - minimalny koszt dotarcia do stacji i z tankowaniem do pełna na tej stacji

    i = 0
    while i < n and S[i] <= L:  # przeglądam stacje, do których mogę dojechać ze startu i nadaje im wartosci początkowe
        F[i] = S[i] * P[i]
        i += 1

    def f(i):
        if F[i] != inf: return F[i]

        x = i - 1
        while x >= 0 and (S[i] - S[x]) <= L:
            F[i] = min(F[i], f(x) + (S[i] - S[x]) * P[i])
            x-=1

        return F[i]

    return f(n-1)



L = 5
S = [1, 2, 3, 6, 8, 10, 15, 18, 19, 20, 25]
P = [3, 6543, 356, 7, 46, 35, 4, 3, 2, 6, 0]
T = 25

print(zad_b2(L, S, P, T))
