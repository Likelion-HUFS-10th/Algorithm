nums = []
max = 0

for num in range(9):
    nums.append(int(input()))

for i in range(9):
    if nums[i] > max :
        max = nums[i]

print(max)
print(nums.index(max)+1)