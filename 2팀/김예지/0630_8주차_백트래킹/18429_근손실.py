from itertools import permutations

N, K = map(int, input().split())
A = list(map(int, input().split()))
final = []

for temp in permutations(A, N):
  sum = 500
  cnt = 0
  for i in range(N):
    sum +=  temp[i] - K
    if sum < 500:
      cnt += 1
  if cnt == 0:
    final.append(temp)

print(len(final))