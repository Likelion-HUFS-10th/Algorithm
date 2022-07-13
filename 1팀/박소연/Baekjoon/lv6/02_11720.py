# 첫째줄 : 숫자 개수 n
# 둘째줄 : n개의 숫자 -> 공백X
# 출력 : n개의 숫자의 합

n = int(input())
total = 0
arr = list(map(int, input()))

for i in range(n):
  total += arr[i]

print(total)