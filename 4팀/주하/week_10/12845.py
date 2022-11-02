# 모두의 마블

n = int(input())
level = list(map(int,input().split()))

level.sort(reverse=True)

large = level[0]
result = 0

for i in range(1, n):
    result += large + level[i]

print(result)