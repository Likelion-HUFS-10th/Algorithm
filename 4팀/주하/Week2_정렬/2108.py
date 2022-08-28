import sys
from collections import Counter   # 최빈값 counter 모듈 사용

n = int(input())
arr = [int(input()) for _ in range (n)]
arr.sort()

print(round(sum(arr)/n))   # 산술평균
print(arr[(n-1)//2])       # 중앙값

cnt = Counter(arr).most_common()     # 최빈값
if len(cnt)>1 and cnt[0][1]==cnt[1][1]:
  print(cnt[1][0])
else :
  print(cnt[0][0])

print(max(arr)-min(arr))   # 범위
