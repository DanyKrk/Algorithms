from math import inf

L = 5
S = [1, 2   , 3  , 6, 8 , 10, 15, 18, 19, 20]
P = [3, 6543, 356, 7, 46, 35, 4 , 3 , 2 , 6]
T = 25


def zad_a(L, S, P, T):
    n = len(S)
    curr_station = -1
    curr_pos = 0
    curr_vol = L
    refuelings_counter = 0
    while (True):
        if T - curr_pos <= curr_vol: return refuelings_counter # jak T jest w moim zasięgu - idę tam
        if curr_station == n-1: return "nie da sie dojechac do T" #jestem na ostatniej stacji i nie moglem dojechac do T

        i = curr_station + 1
        while i < n and S[i] - curr_pos <= curr_vol: i += 1 #T nie jest w zasięgu - wyszukuje najdalszą możliwą stację
        i -= 1
        curr_pos = S[i] # idę na tą stację
        curr_station = i
        refuelings_counter += 1

def zad_b1(L, S, P, T):
    n = len(S)
    F = [[inf] * (L+1) for i in range(n)] # F[i][j] - najmniejszy koszt, za pomocą którego mogę dojechać do stacji i tak, żeby po tankowaniu mieć j litrów paliwa

    i = 0 #wypełniam wszytskie pola w tablicy F, które mogę uzupełnić jadąc bezpośrednio z początku drogi
    while S[i] <= L:
        for j in range(L-S[i], L+1, 1): F[i][j] = P[i] * (j-(L-S[i]))
        i += 1


    def f(i,j):
        if F[i][j] != inf and S[i]>L: return F[i][j] # jak S[i] <= L są tam wartości początkowe, musze sprawdzić czy nie ma lepszych

        a = i-1
        while a >= 0 and S[i] - S[a] <= L: # wyznaczam F[i][j]
            for b in range(S[i]-S[a], L+1, 1):
                F[i][j] = min(F[i][j], F[a][b] + P[i]*(j-(b-(S[i]-S[a]))))
            a-=1
        return F[i][j]

    min_res = inf #znajduję najlepsze rozwiązanie
    i = n-1
    while i >= 0 and T - S[i] <= L:
        for j in range(T-S[i], L+1, 1):
            min_res = min(min_res, f(i,j))
        i-=1

    return min_res





def zad_b2(L, S, P, T):
    n = len(S)
    curr_station_id = -1
    curr_pos = 0
    curr_vol = L
    spent = 0
    while (True):
        if T - curr_pos <= curr_vol: return spent # jak T jest w moim zasięgu - idę tam
        if curr_station_id == n-1: return "T is unachievable" #jestem na ostatniej stacji i nie moglem dojechac do T

        i = curr_station_id + 1
        min_price = inf
        cheapest_station_id = inf
        while i < n and S[i] - curr_pos <= curr_vol: #T nie jest w zasięgu - wyszukuje najtańszą możliwą stację w zasięgu
            if P[i] <= min_price:
                min_price = P[i]
                cheapest_station_id = i
            i += 1
        spent += P[cheapest_station_id] * (S[cheapest_station_id] - curr_pos)
        curr_pos = S[cheapest_station_id] # idę na tą stację
        print(curr_pos)
        curr_station_id = cheapest_station_id




print(zad_b1(L, S, P, T))
