a, b = map(int, input().split())
sum = 0
list = []
i = 1
while len(list) < b:
    for j in range(i):
        list.append(i)
    i += 1

for k in range(a, b+1):
    sum += list[k-1]

print(sum)