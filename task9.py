from random import randint

n, m = 4, 5
arr = [[randint(1, 9) for j in range(m)] for i in range(n)]

for row in arr:
    print(*row)
print()

sum_col = [0] * m
for i in range(n):
    for j in range(m):
        sum_col[j] += arr[i][j]

s = sum(sum_col)
for j in range(m):
    sum_col[j] = round(sum_col[j] / s, 3)
arr.append(sum_col)

for row in arr:
    print(*row)