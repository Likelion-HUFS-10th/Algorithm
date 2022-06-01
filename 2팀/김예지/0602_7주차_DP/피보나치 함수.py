# def fib(n):
#   global zero_cnt
#   global one_cnt
#   if n == 0:
#     zero_cnt += 1
#     return 0
#   elif n == 1:
#     one_cnt += 1
#     return 1
#   else:
#     return (fib(n-1)+fib(n-2))

# for i in range(int(input())):
#   N = int(input())
#   zero_cnt = one_cnt = 0
#   fib(N)
#   print(zero_cnt, one_cnt)

zero = [1, 0, 1]
one = [0, 1, 1]

def cnt(n):
  length = len(zero)
  if length <= n:
    for i in range(length, n+1):
      zero.append(zero[i-1]+zero[i-2])
      one.append(one[i-1]+one[i-2])
  print("%d %d" %(zero[n], one[n]))

for i in range(int(input())):
  n = int(input())
  cnt(n)