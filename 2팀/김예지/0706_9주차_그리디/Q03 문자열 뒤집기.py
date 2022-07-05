# 15:30
str_lst = [w for w in input()]
prev = int(str_lst[0])
cnt = [0, 0]
cnt[prev] += 1

for data in str_lst:
  data = int(data)
  if data != prev:
    cnt[data] += 1
  prev = data

print(min(cnt))

