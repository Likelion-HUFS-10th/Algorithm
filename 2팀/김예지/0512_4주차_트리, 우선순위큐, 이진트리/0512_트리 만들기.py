# 14244 트리 만들기

n, m = map(int, input().split())

if m == 2:
  for i in range(n-1):
    print(i, i+1)
else:
  last = m
  print(0, 1)
  for i in range(2, last+1):
    print(1, i)
  for i in range(last+1, n):
    print(last, i)
    last += 1
    