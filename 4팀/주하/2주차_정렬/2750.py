n = int(input())
num = [ int(input()) for i in range (n) ]

for i in range (n-1):                   # 0부터 n-1까지 돌며 오른쪽 수와 크기 비교
  for j in range (i+1, n):
    if num[i]>num[j]:
       num[i],num[j] = num[j],num[i]    # 크기 비교해서 자리 바꾸기

for k in num:
    print (k)
