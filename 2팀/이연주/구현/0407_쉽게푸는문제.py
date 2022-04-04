import math
a, b = tuple(map(int, input().split()))
arr = []

for i in range(1, 46):
    for j in range(i):
        arr.append(i)

print(sum(arr[a-1:b]))