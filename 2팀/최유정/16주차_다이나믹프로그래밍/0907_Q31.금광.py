for _ in range(int(input())):
    n, m = map(int, input().split())
    gold = list(map(int, input().split()))

    def list_chunk(lst, n):
        return [lst[i:i+n] for i in range(0, len(lst), n)]

    gold = list_chunk(gold, m)
    dp = list_chunk([0]*(n+2)*m, m)
    for i in range(n):
        dp[i+1][0] = gold[i][0]

    for x in range(1, m):
        for y in range(1, n):
            dp[y][x] = max(dp[y+2][x-1], dp[y+1][x-1], dp[y][x-1]) + gold[y][x]


    max_gold = dp[0][m-1]
    for a in range(n-1):
        max_gold = max(max_gold, dp[a+1][m-1])

    print(max_gold)