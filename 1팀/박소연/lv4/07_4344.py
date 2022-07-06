# 평균이 넘는 학생 비율 반올림해서 셋째 자리까지 출력
# C명의 평균 구하기 -> 평균보다 높은 학생 수 count -> 평균보다 높은 학생수 / C * 100
# round 함수는 딱 떨어질 경우 소수점 첫째자리까지 밖에 출력 안됨
# so, 포맷팅으로 소수점 자리수 지정 "{:.3f}".format(변수)

num = int(input())
input_list = []

for i in range(num):
  input_list.append(list(map(int, input().split())))

for elem in input_list:
  cnt = 0
  std_num = elem[0]
  std_score = elem[1:]
  std_average = sum(std_score) / std_num
  for score in std_score:
    if score > std_average:
      cnt += 1
  over_average = round(cnt / std_num * 100, 3)
  print("{:.3f}%".format(over_average))
