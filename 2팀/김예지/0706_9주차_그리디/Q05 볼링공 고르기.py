from itertools import combinations

N, M = map(int, input().split())
kg_lst = list(map(int, input().split()))

cnt = 0

for i in combinations(kg_lst, 2):
  if i[0] != i[1]:
    cnt +=1

print(cnt)