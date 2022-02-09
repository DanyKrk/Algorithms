A = [1,4,6,2,4,423,3,634,6,5,346,45,6,437,5456]
t = 345

def zad2(A, t):
    n = len(A)
    F = [[False] * (t+1) for i in range(n)] # F[i][j] - czy liczbę j można utworzyć z liczb o indeksach nie większych niż i
    for i in range(n):
        if A[i] <= t:
            F[i][A[i]] = True

    for i in range(1,n):
        for num in range(t+1):
            if num - A[i] >= 0 and F[i-1][num-A[i]]:
                F[i][num] = F[i-1][num-A[i]]
            elif F[i - 1][num]:
                F[i][num] = F[i - 1][num]

    return F[n-1][t]

print(zad2(A,t))