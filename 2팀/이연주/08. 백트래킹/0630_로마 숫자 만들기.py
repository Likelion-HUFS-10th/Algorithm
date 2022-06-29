from itertools import combinations_with_replacement

li = [1, 5, 10, 50]
n = int(input())
answer = 0
items = list(combinations_with_replacement(li, n))
answer = set()
for item in items:
    answer.add(sum(item))
if n == 1:
    answer = li
print(len(answer))