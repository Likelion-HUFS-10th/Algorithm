from collections import deque

n = int(input())
a = list(map(int, input().split()))
a = deque(a)
number = [
    i + 1
    for i in range(n)
]
number = deque(number)

results = []

pointer = 0

for i in range(n):
    pointer = a[0]
    a.popleft()
    pop = number.popleft()
    results.append(str(pop))
    if pointer >= 0:
        a.rotate(-(pointer - 1))
        number.rotate(-(pointer - 1))
    elif pointer < 0:
        a.rotate(-(pointer))
        number.rotate(-(pointer))

print(' '.join(results))