nums = []
num = 0

for _ in range(10):
    num = int(input())
    nums.append(num%42)

nums = set(nums)
print(len(nums))