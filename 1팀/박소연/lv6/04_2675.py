# 문자열 반복

t = int(input())
new_s = ""

for i in range(t):
  r, s = input().split()
  for j in s:
    new_s += j * int(r)
  print(new_s)
  new_s = ""