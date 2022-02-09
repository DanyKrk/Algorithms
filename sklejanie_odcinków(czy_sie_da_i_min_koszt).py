from math import *

def zad7_1(ranges,F,a,b):

    if F[a][b] != -1: return F[a][b]
    value = 0
    for i in range(a+1,b):
        value = max(value, (zad7_1(ranges,F,a,i)+zad7_1(ranges,F,i,b))//2)
    F[a][b] = value
    return value


ranges=[[1,2],[4,6],[2,7],[3,4],[6,8]]
max_range_end = 0
for el in ranges: max_range_end = max(max_range_end,el[1])
F = [[-1]*(max_range_end+1) for i in range((max_range_end+1))]
for el in ranges: F[el[0]][el[1]] = 1

print(zad7_1(ranges, F, 4,8))



def zad7_2(ranges,F,a,b):
    if F[a][b] != -1: return F[a][b]
    value = inf
    for i in range(a+1,b):
        x = zad7_1(ranges,F,a,i)
        y = zad7_1(ranges,F,i,b)
        value = min(value,x+y)
    F[a][b] = value
    return value

ranges=[[1,2,1],[4,6,1],[2,7,1],[3,4,1],[6,8,1]]
max_range_end = 0
for el in ranges: max_range_end = max(max_range_end,el[1])
F = [[-1]*(max_range_end+1) for i in range((max_range_end+1))]
for el in ranges: F[el[0]][el[1]] = el[2]

print(zad7_2(ranges, F, 4,8))