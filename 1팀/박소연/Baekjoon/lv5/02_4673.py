# 셀프 넘버
# 1~10000 집합 - 생성자가 있는 집합

whole_set = set(range(1, 10000))
notself_set = set()

for elem in range(1, 10001):
  for num in str(elem):
    elem += int(num)
  notself_set.add(elem)

self_set = sorted(whole_set - notself_set) # 정렬해줘야 함

for elem in self_set:
  print(elem)
