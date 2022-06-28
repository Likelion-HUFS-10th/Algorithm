import sys
input = sys.stdin.readline

def back(cnt, start):
    global result
    if cnt == n:
        num[result] = 1
        return
    for i in range(start, 4):
        result += roma[i]
        back(cnt + 1, i)
        result -= roma[i]

n = int(input())
roma = [1, 5, 10, 50]
result = 0
num = [0] * (50 * 20 + 1)
back(0, 0)
print(sum(num))