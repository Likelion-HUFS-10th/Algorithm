# 23:08 | 3.2819483280181885 | 5.049158811569214 | 2.845322608947754 | day 2 | 10:56


N, M, K = map(int, input().split())
num_lst = list(map(int, input().split()))
sum = 0

num_lst.sort()
a, b = num_lst[-1], num_lst[-2]

num_cycle = a * K + b

if M == 0:
  print(0)
else:
  if M % (K + 1) == 0:
    print(int(num_cycle * M / (K+1)))
  else:
    print(int(num_cycle * (M // (K+1)) + a * (M % (K+1))))

