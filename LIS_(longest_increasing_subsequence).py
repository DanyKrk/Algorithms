def LIS(A):
    n = len(A)
    F = [1 for i in range(n)]
    P = [-1 for i in range(n)]

    for i in range(n):
        for j in range(i):
            if(A[j]<A[i] and F[j]+1 > F[i]):
                F[i] = F[j]+1
                P[i] = j
    max_ind = 0
    max_res = 0

    for i in range(n):
        if(F[i]>max_res):
            max_ind = i
            max_res = F[i]
    return F[max_ind],max_ind, F, P

def printres(A, P, i):
    if(P[i]>=0):
        printres(A, P, P[i])
    print(A[i], end=" ")

A = [1,3,4,85,4,36,36,5,63,62,7,2,456,425,6,54,53,45,26,45,7,35678,2456,365,7,27,54,673,6,453,63,4567,3,76,356,3,7,34567,3456,7,347,35467,0]

l, ind, F, P = LIS(A)
n = len(A)

print(l)
printres(A,P,ind)
print(" ")
print(F)
print(P)



