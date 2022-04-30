# a + b에 케이스 번호 추가

t = int(input())

for i in range(1, t+1):
  a, b = map(int, input().split())
  print("Case #%d: %d" % (i, a + b))