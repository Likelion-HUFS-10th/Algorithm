str_lst = [w for w in input()]
result = 0

for data in str_lst:
  data = int(data)
  if data <= 1 or result <= 1:
    result += data
  else:
    result *= data

print(result)

