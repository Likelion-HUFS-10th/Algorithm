# 숫자 - 알파벳 리스트 매칭
# 각 숫자별 시간 리스트
# 걸리는 시간 리스트 -> 원소 합

word_arr = list(input())
time_arr = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
time_sum = []

for i in range(len(word_arr)):
  if word_arr[i] == 1:
    time_sum.append(2)
  elif word_arr[i] in ["A", "B", "C"]:
    time_sum.append(time_arr[1])
  elif word_arr[i] in ["D", "E", "F"]:
    time_sum.append(time_arr[2])
  elif word_arr[i] in ["G", "H", "I"]:
    time_sum.append(time_arr[3])
  elif word_arr[i] in ["J", "K", "L"]:
    time_sum.append(time_arr[4])
  elif word_arr[i] in ["M", "N", "O"]:
    time_sum.append(time_arr[5])
  elif word_arr[i] in ["P", "Q", "R", "S"]:
    time_sum.append(time_arr[6])
  elif word_arr[i] in ["T", "U", "V"]:
    time_sum.append(time_arr[7])
  elif word_arr[i] in ["W", "X", "Y", "Z"]:
    time_sum.append(time_arr[8])
  else:
    time_sum.append(time_arr[9])

time = sum(time_sum)
print(time)