# 한수 구하기
# 한수 : 각 자리가 등차수열을 이루는 수
# N보다 작거나 같은 한수의 개수 출력
# 100보다 작으면 무조건 한수
# 100보다 같거나 크면 연속된 두 인덱스 차가 같아야 등차수열

def find_hansu(input_num):
  cnt = 0
  for i in range(1, input_num+1):
    if i < 100:
      cnt += 1
    else:
      i = str(i)
      if (int(i[0]) - int(i[1]) == int(i[1]) - int(i[2])):
        cnt += 1
  return cnt

num = int(input())
print(find_hansu(num))
