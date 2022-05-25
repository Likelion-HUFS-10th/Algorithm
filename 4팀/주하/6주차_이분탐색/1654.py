'''
랜선 자르기

'''
import sys

k,n =map(int,sys.stdin.readline().split())
lines = [int(sys.stdin.readline()) for _ in range(k)]
min_line, max_line = 1, max(lines)   #랜선 최소 개수와 최대 개수

while min_line <= max_line:
    mid = (min_line + max_line) // 2
    cnt = 0          #랜선 개수
    for i in lines:
        cnt += i // mid             # 분할된 랜선 -> 개수 추가하기

    if cnt >= n:
        min_line = mid + 1

    else:
        max_line = mid - 1

print(max_line)

