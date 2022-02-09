def exist(A,s):
    n = len(A)
    F = [[False] * (s+1) for i in range(n)]
    for i in range(n):
        if A[i] <= s:
            F[i][A[i]] = True
    for i in range(1,n):
        for j in range(s+1):
            if F[i-1][j]: F[i][j] = True
            if j-A[i]>=0 and F[i-1][j-A[i]]:
                F[i][j] = True
    return F[n-1][s]

A = [2,4,6,7]
print(exist(A,5))