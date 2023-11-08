n = int(input())
m = int(input())
arr = [[0 if (i + j)%2 else (i * m + j)//2+1 for j in range(m)] for i in range(n)]
for i in arr:
    print(i)