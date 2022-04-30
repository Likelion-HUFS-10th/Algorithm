# 더하기 사이클
# 질문1 : 주어진 수가 10보다 작은 경우를 안따져도 되는가? 밑의 코드는 어디가 잘못된건지?


first = int(input())
num = first
cnt = 0

while True:
  if num < 10:
    num *= 10
    new = (num%10) * 10 + (num//10 + num%10) % 10
  else:
    new = (new%10) * 10 + (new//10 + new%10) % 10
  cnt += 1
  if num == first:
    break
  num = new

print(cnt)

# -----------------------------------------------------

first = int(input())
num = first
cnt = 0

while True:
  new = ((num%10) * 10) + (((num//10) + (num%10))%10)
  cnt += 1
  if new == first:
    break
  num = new

print(cnt)