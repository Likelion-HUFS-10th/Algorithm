'''
ATM 문제

'''


n = int(input())
line = list(map(int,input().split()))

line.sort()       # 오름차순 정렬
line_sum = 0
result = 0

# 1 2 3 3 4

for i in range(n):
    line_sum += line[i]   # 1 3 6 9 13
    result += line_sum

print(result)