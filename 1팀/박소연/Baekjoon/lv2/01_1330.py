# 두 수 비교 -> 뺄셈 결과 0과 비교

a, b = map(int, input().split())

if a - b > 0:
  print(">")
elif a - b < 0:
  print("<")
else:
  print("==")