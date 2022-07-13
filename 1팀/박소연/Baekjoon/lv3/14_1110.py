# 더하기 사이클
# 질문1 : 주어진 수가 10보다 작은 경우를 안따져도 되는가? 밑의 코드는 어디가 잘못된건지?
# 피드백 : 되도록 종료조건을 while문의 맨 마지막에 -> but 항상 그런건 아님
# 나머지로 구현하면 어차피 조건이 당연하게 해결됨 so, 안따져도 ok

first = int(input())
num = first
new = 0
cnt = 0

while True:
  if num < 10:
    num *= 10
    new = (num%10) * 10 + (num//10 + num%10) % 10
  else:
    new = (num%10) * 10 + (num//10 + num%10) % 10
  cnt += 1
  num = new
  if num == first: 
    break

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