import sys
n, m = map(int,sys.stdin.readline().split())
n_list =  list(map(int,sys.stdin.readline().split()))
min_line, max_line = 1 , max(n_list)

while min_line <= max_line:
    mid = (min_line + max_line) // 2
    cnt = 0
    for i in n_list:
        if i > mid:
            cnt += i -mid

    if cnt >= m:
        min_line = mid + 1


    else:
        max_line = mid - 1

print(max_line)