import sys
input = sys.stdin.readline

x = int(input())   # 구하려는 번호

line = 0   # 대각선 넘버링
max_num = 0   # 대각선 내 가장 큰 번호

while max_num < x:
    line += 1
    max_num += line

if line % 2 == 0:
    up = line - (max_num - x)
    down = 1 + (max_num - x)
else:
    up = 1 + (max_num - x)
    down = line - (max_num - x)
    
print("%d/%d" %(up, down))
