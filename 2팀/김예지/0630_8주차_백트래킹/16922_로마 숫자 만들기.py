# N = int(input())
# lst = []
# for i in range(N+1):
#     for j in range(N+1-i):
#         for k in range(N+1-i-j):
#             t = N-i-j-k
#             sum = i + 5*j + 10*k + 50*t
#             lst.append(sum)
            
# print(len(set(lst)))

from itertools import combinations_with_replacement

N = int(input())
lst = []
rom = [1, 5, 10, 50]

for temp in combinations_with_replacement(rom, N):
  lst.append(sum(temp))
print(len(set(lst)))