t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    maxi = 0
    profit = 0
    for i in range(n - 1, -1, -1):
        if a[i] > maxi:
            maxi = a[i]
        else:
            profit += maxi - a[i]
    print(profit)