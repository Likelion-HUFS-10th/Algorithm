# 연속된 O의 개수가 맞은 문제 수


num = int(input())
ox_list = []

for i in range(num):
  input_ox = input()
  ox_list.append(input_ox)

for elem in ox_list:
  cnt, total = 0, 0
  for ox in elem:
    if ox == "O":
      cnt += 1
      total += cnt
    elif ox == "X":
      cnt = 0
      total += cnt
  print(total)
