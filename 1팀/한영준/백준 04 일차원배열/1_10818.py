n = int(input())
nums = list(map(int, input().split()))
max = -1000000
min = 1000000

for i in range(n) :
    if nums[i] > max :
        max = nums[i]
    if nums[i] < min :
        min = nums[i]

print(min , max)