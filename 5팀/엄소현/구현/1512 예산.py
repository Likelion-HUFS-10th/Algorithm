import sys
input = sys.stdin.readline

n = int(input())   # 지방의 수
reqs = list((map(int, input().split())))   # 각 지방의 예산 요청
m = int(input())   # 총 예산

left = 0
right = max(reqs)

while left <= right:
  mid = (left + right) // 2   # 상한액
  req_sum = 0
  for req in reqs:
    if req > mid:   # 요청액이 상한액보다 클 경우 상한액으로 계산
      req_sum += mid
    else:   # 요청액이 상한액보다 작을 경우 요청액으로 계산
      req_sum += req
  if req_sum > m:   # 요청액 합이 총 예산보다 클 경우
    right = mid - 1
  else:
    left = mid + 1
print(right)
