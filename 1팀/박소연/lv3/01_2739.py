# 구구단 -> for문(i 1~9)

a = int(input())

for i in range(1, 10):
  print("%d * %d = %d" % (a, i, a*i))