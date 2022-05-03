import sys
input = sys.stdin.readline

n = int(input())
a = [int((input())) for _ in range(n)]
answer = 1

maximum = a[-1]
for i in range(n-1, -1, -1):
    if maximum < a[i]:
        maximum = a[i]
        answer += 1

print(answer)
