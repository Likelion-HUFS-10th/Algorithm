# T = int(input())

for T in range(int(input())):
    n, m = map(int, input().split())
    golds = list(map(int, input().split()))
    array = [golds[i*m : (i+1)*m] for i in range(len(golds) // m)]
    # -------------- 해답 ----------------
    for j in range(1, m):
        for i in range(n):
            if i == 0:
                left_up = 0
            else:
                left_up = array[i - 1][j - 1]
            if i == n - 1:
                left_down = 0
            else:
                left_down = array[i + 1][j - 1]
            left = array[i][j - 1]
            array[i][j] = array[i][j] + max(left_up, left_down, left)

    result = 0
    for i in range(n):
        result = max(result, array[i][m - 1])
    print(result)


