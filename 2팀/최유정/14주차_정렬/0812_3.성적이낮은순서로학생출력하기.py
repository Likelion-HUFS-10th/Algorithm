n = int(input())
ns = {}
for _ in range(n):
    name, score = input().split()
    score = int(score)
    ns[name] = score

sort_ns = sorted(ns.items(), key=lambda x:x[1])
for i in sort_ns:
    print(i[0], end=' ')