# 15:38
N = list(input())
num_lst = [str(i) for i in range(0, 10)]
nums = []
sum = 0

for i in N:
  if i in num_lst:
    nums.append(i)

alpha_str = [w for w in N if w.isalpha()]
alpha_str.sort()

for i in alpha_str:
  print(i, end = "")

for i in nums:
  sum += int(i)

print(sum)
