# 문자열 거꾸로 -> int -> 두 수 중 max 출력

a, b = map(list, input().split())
a.reverse()
b.reverse()

a, b = list(map(int, a)), list(map(int, b))
a = a[0] * 100 + a[1] * 10 + a[2]
b = b[0] * 100 + b[1] * 10 + b[2]

if a > b:
  print(a)
else:
  print(b)