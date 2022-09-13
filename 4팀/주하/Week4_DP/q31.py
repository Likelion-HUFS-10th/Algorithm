#    i
# j  0  1  2  3
# 0  1  3  3  2
# 1  2  1  4  1
# 2  0  6  4  7
# 규칙 찾기 ! -> m번에 걸쳐서 매번 오른쪽 위, 오른쪽, 오른쪽아래
num = int(input())

for _ in range(num):
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    d = []
    idx = 0
    for _ in range(n):
        d.append(arr[idx:idx+m])
        idx += m

    for j in range(1, m):
        for i in range(n):
            if i == 0:
                d[i][j] = d[i][j] + max(d[i][j-1], d[i+1][j-1])
            elif i == n-1:
                d[i][j] = d[i][j] + max(d[i-1][j-1], d[i][j-1])
            else:
                d[i][j] = d[i][j] + max(d[i-1][j-1], d[i][j-1], d[i+1][j-1])

    result = 0
    for i in range(n):
        result = max(result, d[i][m-1])
    print(result)
