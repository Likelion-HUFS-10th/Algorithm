n = int(input())
coin = list(map(int, input().split()))
result = []

for i in range(n):
    for j in range(i+1, n+1):
        result.append(sum(coin[i:j]))
result = set(result)
target = 1
for i in result:
    if i != target:
        print(target)
        break
    target += 1