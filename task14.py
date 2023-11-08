from random import randint

m = int(input('Size:'))
a = [[randint(0, 1) for j in range(m)] for i in range(m)]
print('Source matrix:')
for row in a:
    print(*row)
print()
for row in a:
    row.append(sum(row)%2)
print('End matrix:')
for row in a:
    print(*row)