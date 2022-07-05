n = int(input())
coin_lst = [500, 100, 50, 10]
sum = 0

for coin in coin_lst:
  while True:
    n -= coin
    sum += 1
    if n < coin:
      break
print(sum)
