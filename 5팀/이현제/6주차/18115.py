from collections import deque

n = int(input())
teq = deque(map(int, input().split()))
card = [i for i in range(1, n + 1)]
card = deque(card)
result = deque()

while len(teq) != 0:
    teq_num = teq.pop()
    target = card.popleft()

    if teq_num == 1:
        result.appendleft(target)
    elif teq_num == 2:
        result.insert(1, target)
    else:
        result.append(target)

for i in result:
    print(i, end=' ')