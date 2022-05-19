from collections import deque

n, k = tuple(map(int, input().split()))
a = [
    i + 1
    for i in range(n)
]
a = deque(a)
results = []
while len(a) != 0:
    a.rotate(-(k - 1))
    pop = a.popleft()
    results.append(pop)
    
print('<',end='')
print(*results, sep=', ', end='')
print('>')
