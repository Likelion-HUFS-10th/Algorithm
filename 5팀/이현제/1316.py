n = int(input())
cnt = 0
for _ in range(n):
    a = list(input())
    length = len(a)
    i = 0
    for target in a:
        if i + 2 > length:
            break
        if (a[i + 1] != target) and (target in a[i + 2:]):
            cnt += 1
            break
        else:
            i += 1
            print(f"{target}/{i}")
print(n - cnt)
