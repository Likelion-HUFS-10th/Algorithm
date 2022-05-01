# 2605 줄 세우기

# by oneself
N = int(input())
row = []
choice = list(map(int, input().split()))

for i in range(0, N):
    idx = i
    idx = idx - choice[i]
    row.insert(idx, i+1)
    
for r in row:
    print(r, end=" ")