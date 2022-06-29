from itertools import permutations
arr = [i for i in range(1, 9)]
n, m = list(map(int, input().split()))

this = arr[:n]
answer = list(permutations(this, m))
for a in answer:
    print(*a)