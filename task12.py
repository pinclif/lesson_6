m = [
    [2, 9, 5, 8, 9],
    [7, 1, 3, 2, 4],
    [4, 6, 0, 1, 6]
]
n = 3

for num, column in enumerate(zip(*m)):
    if n in column:
        indices = [idx for idx, _ in enumerate(column) if _ == n]
        print('The column {} contains {}'.format(num, n, indices))
    else:
        print('The column {} does not contain {}'.format(num, n))