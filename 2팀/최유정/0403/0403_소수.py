m = int(input())
n = int(input())
list = []
for i in range(m, n+1):
    for j in range(2, i):
        if i % j == 0:
            break
        if j == (i - 1):
            list.append(i)

if len(list) == 0:
    print(-1)
else:
    print(sum(list))
    print(list[0])