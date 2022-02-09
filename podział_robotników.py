# Wartość podziału - max wartość minimalnego przedziału
#F[i][j] - maksymalna wartość podziału na i pracowniów płotów od 0 do j włącznie
# F[i][j] = max po o (min(F[i-1][j-0], suma plotów od j-0+1 do końca płotów))

def find_highest_division_value(P,k):
    n = len(P)
    F = [[0] * n for i in range(k+1)]
    F[1][0] = P[0]
    for i in range(n):
        F[1][i] = F[1][i-1] + P[i]
    for i in range(2,k+1):
        for j in range(i,n):
            o = 1
            while j-o>=0:
                contestant = min(F[i-1][j-o], F[1][n-1] - F[1][j-o])
                if contestant > F[i][j]:
                    F[i][j] = contestant
                o += 1
    return F[k][n-1]

P = [4,6,2,6,6,3,3,6,4,5,5,4,2,4,2,4,2,3,2,6,3,5,6,3,5,4,6,2,5,6,2]
print(find_highest_division_value(P,20))