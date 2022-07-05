# 18:40
from itertools import combinations

N = int(input())
num_lst = list(map(int, input().split()))

sum_lst = []
for i in range(1, N+1):
  for j in combinations(num_lst, i):
    sum_lst.append(sum(j))

result_lst = list(set(sum_lst))
result_lst.sort()

start = 0
for data in result_lst:
  if data - start != 1:
    result = data
    break
  start += 1

print(result-1)

