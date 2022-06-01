from tkinter import N


A = int(input())
lst = list(map(int, input().split()))

dp = [1] * A
for i in range(A):
  for j in range(i):
    if lst[j] < lst[i]:
      dp[i] = max(dp[i], dp[j]+1)

print(max(dp))