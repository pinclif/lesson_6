def diagonal(l,c):
    s = 0
    i = 0
    while i < N:
        if c == '1':
            s += l[i][i]
        else:
            s += l[i][N-i-1]
        i += 1
    return s

from random import random
N = 9
a = []
for i in range(N):
    b = []
    for j in range(N):
        n = int(random()*10)
        b.append(n)
        print('%3d' % n, end='')
    a.append(b)
    print()

ch = input("Main diagonal (1) or Side diagonal (2): ")
if ch == '1' or ch == '2':
    summa = diagonal(a,ch)
    print(summa)