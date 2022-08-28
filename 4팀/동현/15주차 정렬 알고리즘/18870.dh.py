n = int(input())
array = list(map(int, input().split()))
result = []
array_set = sorted(list(set(array)))
for i in array:
    result.append(array_set.index(i))
for j in result:
    print(j, end=' ')