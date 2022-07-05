import math
n = input()
num = list(map(int, n))
cnt = 0

for i in range(len(num) - 1):
    if num[i] != num[i+1]:
        cnt += 1

print(math.ceil(cnt/2))
