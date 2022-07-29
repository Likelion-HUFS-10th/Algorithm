import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))

nums.sort()

def good_number(temp, k):
  left = 0
  right = n - 2
  while left < right:
    if temp[left] + temp[right] == k:
      return True
    elif temp[left] + temp[right] < k:
      left += 1
    else:
      right -= 1
  return False

cnt = 0
for i in range(n):
  if good_number(nums[:i]+nums[i+1:], nums[i]):
    cnt += 1

print(cnt)