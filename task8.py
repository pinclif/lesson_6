from random import random
m = int(input())
n = int(input())
a = []
for i in range(n):
    b = []
    for j in range(m):
        b.append(int(random()*50) - 25)
        print("%4d" % b[j], end='')
    a.append(b)
    print()
min_mx = 25
for i in range(n):
    min_i = min(a[i])
    if min_i < min_mx:
        min_mx = min_i
print(min_mx)
for i in range(n):
    for j in range(m):
        if min_mx == a[i][j]:
            print('Row: %d, col: %d' % (i+1,j+1))

