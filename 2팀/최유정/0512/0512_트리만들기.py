n, m = map(int, input().split())

if m == 2:
    for i in range(n-1):
        print(i, i+1)
else:
    for i in range(n-m):
        print(i, i+1)
        if i == n-m-1:
            p = i+1
    for j in range(n-m+1, n):
        print(p, j)