import sys
input = sys.stdin.readline

num = input().strip()
cnt = 0   # 자릿수

for i in range(len(num), 0, -1):
    if len(num) == 1:   # 한 자릿수일 경우
        cnt = int(num)
    else:
        if i == len(num):
            cnt = i * (int(num) - (10 ** (len(num) - 1)) + 1)
        else:
            cnt += i * (9 * (10 ** (i - 1)))

print(cnt)
