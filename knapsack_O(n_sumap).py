def knapsack(W, P, maxw):
    n = len(W)
    maxp = 0
    for i in range(n):
        maxp += P[i]
    F = [[maxw+1]*(maxp+1) for i in range(n)]
    Parent = [[maxw + 1] * (maxp + 1) for i in range(n)]

    for i in range(n):
        F[i][P[i]] = W[i]

    for i in range(1, n):
        for j in range(maxp+1):
            F[i][j] = min(F[i-1][j], F[i][j])
            if j - P[i] >= 0:
                F[i][j] = min(F[i][j], (F[i-1][j-P[i]] + W[i]))

    for i in range(maxp, -1, -1):
        if F[n-1][i] != maxw+1:
            return i, F, maxp

def getsolution(F, W, P, i,j, maxp):
    if i == 0:
        if F[i][j] == maxp+1:
            return []
        print(j)
        return [i]

    if F[i][j] == (F[i-1][j-P[i]] + W[i]):
        return getsolution(F, W, P, i-1, j-P[i], maxp)+[i]
    return getsolution(F, W, P, i-1, j, maxp)



W = [4, 3, 2, 2, 15, 1, 5]
P = [5, 7, 9, 3, 20, 3, 15]
maxw = 6
n = len(W)

res, F, maxp = knapsack(W, P, maxw)
print(res)
print(getsolution(F,W,P,n-1,res, maxp+1))
for i in range(n):
    print(F[i])
