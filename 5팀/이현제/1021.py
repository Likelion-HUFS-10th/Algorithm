from collections import deque

n, m = tuple(map(int, input().split()))
target = list(map(int, input().split()))
target = deque(target)
all = [
    i + 1
    for i in range(n)
]
all = deque(all)
cnt = 0

while len(target) != 0 :
    if all[0] == target[0]:
        all.popleft()
        target.popleft()
    elif all[0] != target[0] and all.index(target[0]) <= (len(all) // 2):
        all.rotate(-1)
        cnt += 1
    elif all[0] != target[0] and all.index(target[0]) > (len(all) // 2):
        all.rotate()
        cnt += 1
print(cnt)

