import sys
input = sys.stdin.readline

n, m = map(int, input().split())   # n: 수열 수, m: 합이 나와야 하는 값
seq = list(map(int, input().split()))

i, j = 0, 0   # 포인터
cnt = 0   # 경우의 수

while i <= j and j <= n:
    now_sum = sum(seq[i:j])

    if now_sum == m:
        cnt += 1
        i += 1
        j += 1
    elif now_sum < m:
        j += 1
    else:
        i += 1

print(cnt)
