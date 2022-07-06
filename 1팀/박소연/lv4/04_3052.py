# 입력받은 10개의 수를 42로 나눈 나머지 중 서로 다른 값이 몇 개 있는지
# 집합으로 형변환(중복제거) -> 집합 길이

input_list = []
cnt = 0

for i in range(10):
  num = int(input())
  input_list.append(num % 42)

print(len(set(input_list)))