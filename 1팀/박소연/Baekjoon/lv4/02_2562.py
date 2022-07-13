# 9개의 서로 다른 자연수 중 최댓값을 찾고 몇번째 수인지 구하기
# 내장함수 : max, index

input_list = []

for i in range(9):
  input_num = int(input())
  input_list.append(input_num)

max = max(input_list)
print(max)
print(input_list.index(max) + 1)
