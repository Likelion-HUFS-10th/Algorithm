def calc(i, now_kal, now_taste, max_taste):
    for k in range(i+1, n):
        max_taste = calc(k, now_kal + kal[k], now_taste + taste[k], max_taste)
    if now_kal <= l:
        max_taste = max(max_taste, now_taste)
    return max_taste

t = int(input())   # 테스트 케이스 수

for tk in range(t):
    n, l = map(int, input().split())   # n: 재료 수, l: 제한 칼로리
    taste, kal = [], []
    best = 0
    for i in range(n):
        t, k = map(int, input().split())
        taste.append(t)
        kal.append(k)
    for i in range(n):
        best = max(best, calc(i, kal[i], taste[i], 0))
    print(f'#{tk + 1} {best}')
