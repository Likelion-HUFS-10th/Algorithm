# n번째 줄 -> "" * (n-i) + "*" * i
# 빈칸 n-i개, 별 i개

n = int(input())

for i in range(1, n+1):
  print(" " * (n-i) + "*" * i) # 공백 띄워야함