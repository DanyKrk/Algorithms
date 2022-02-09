def knapsack(W, P, maxw):
    n = len(W)
    F = [[0] * (maxw + 1) for i in range(n)]  # F[i][j] - maksymalny zysk, jaki możemy uzyskaćz przedmiotów od 0 do i, nie przekraczając wagi j
    for i in range(W[0], maxw + 1):
        F[0][i] = P[0]
    for i in range(1, n):
        for j in range(1, maxw + 1):
            F[i][j] = F[i - 1][j]
            if j - W[i] >= 0:
                F[i][j] = max(F[i][j], F[i - 1][j - W[i]] + P[i])
    return F[n - 1][maxw], F


def getsolution(F, W, P, i, w):
    if i == 0:
        if w>=W[0]: return[0]
        return []
    if w>=W[i] and F[i][w] == F[i-1][w - W[i]]+P[i]:
        return getsolution(F, W, P, i-1, w-W[i])+[i]
    return getsolution(F,W,P,i-1,w)

W = [4, 3, 2, 2, 15, 1, 5]
P = [5, 7, 9, 3, 20, 3, 15]
maxw = 6

res, F = knapsack(W, P, maxw)
n = len(F)
max_w = len(F[0]) - 1
print(res)
print(getsolution(F,W,P,n-1,maxw))
for i in range(n):
    print(F[i])