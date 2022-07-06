# 세가지 수를 곱한 결과값에서 0~9까지의 숫자가 몇 번 쓰였는지 count

num1 = int(input())
num2 = int(input())
num3 = int(input())
result = str(num1 * num2 * num3)

for i in range(10):
  cnt = result.count(str(i))
  print(cnt)

