# while문 종료 조건 : a,b가 0, 0

a, b = 100, 100

while a > 0 and b > 0:
  a, b = map(int, input().split())
  if a == b == 0:
    pass # null 연산 -> 아무것도 하지 않는 기능
  else:
    print(a + b)

# --------------------------------------------

while True:
  a, b = map(int, input().split())
  if a == b == 0:
    break
  else:
    print(a + b)