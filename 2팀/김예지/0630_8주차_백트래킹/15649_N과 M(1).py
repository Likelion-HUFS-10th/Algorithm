from itertools import permutations

N, M = map(int, input().split())
num_lst = [i for i in range(1, N+1)]

for temp in permutations(num_lst, M):
  for i in range(M):
    print(temp[i], end=" ")
  print()