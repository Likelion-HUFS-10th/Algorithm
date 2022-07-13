# 삼항 비교
# 2개 같은 경우 : (a,b)(a,c) / (b,c)
# a, b, c, same, count

a, b, c = map(int, input().split())

if a == b == c:
  price = 10000 + a * 1000
elif a == b or a == c :
  price = 1000 + a * 100
elif b == c:
  price = 1000 + b * 100
elif a != b != c:
  price = max([a, b, c]) * 100

print(price)