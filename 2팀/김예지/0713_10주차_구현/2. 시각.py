# 4:33
N = int(input())
cnt = 0

for i in range(N+1):
  for j in range(60):
    for k in range(60):
      if i % 10 == 3 or i // 10 == 3 or j % 10 == 3 or j // 10 == 3 or k % 10 == 3 or k // 10 == 3:
        cnt += 1

print(cnt)
