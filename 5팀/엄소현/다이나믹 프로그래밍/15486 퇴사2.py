import sys
input = sys.stdin.readline

n = int(input())
time = []
pay = []
for _ in range(n):
  t, p = map(int, input().split())
  time.append(t)
  pay.append(p)

profit = [0 for _ in range(n+1)]
for i in range(n-1, -1, -1):
  if i == n-1 and time[i] == 1:
    profit[i] = pay[i]
  elif i + time[i] <= n:
    profit[i] = max(profit[i+1], pay[i] + profit[i+time[i]])
  else:
    profit[i] = profit[i+1]

print(profit[0])