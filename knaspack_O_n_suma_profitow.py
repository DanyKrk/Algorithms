from math import inf


def Knapsack(W,P,maxw):
    n = len(W)
    maxp = 0
    for i in range(n):
        maxp += P[i]

    F = [[inf] * (maxp+1) for i in range(n)] # F[i][j] - minimalna waga za pomocą której można uzyskać profit j biorąc przedmioty 0-i
    for i in range(n):
        F[i][P[i]] = W[i]
    for i in range(1,n):
        for j in range(maxp+1):
            F[i][j] = min(F[i][j],F[i-1][j])
            if j - P[i] >= 0:
                F[i][j] = min(F[i][j], F[i-1][j-P[i]] + W[i])
                if F[i][j] > maxw: F[i][j] = inf
    for j in range(maxp,-1,-1):
        if F[n-1][j] != inf: return j

W = [1,2,3,4,5,6]
P = [4,7,2,5,2,4]

print(Knapsack(W,P,5))
