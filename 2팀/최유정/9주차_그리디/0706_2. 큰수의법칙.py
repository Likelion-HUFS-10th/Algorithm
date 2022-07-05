n, m, k = map(int, input().split())
list_num = list(map(int, input().split()))

list_num.sort()
max_num = list_num[n-1]
s_max_num = list_num[n-2]
cnt, seq = 0, 0

for _ in range(m):
    if seq == k:
        cnt += s_max_num
        seq = 0
    else:
        cnt += max_num
        seq += 1

print(cnt)