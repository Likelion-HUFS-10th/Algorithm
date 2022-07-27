n = int(input())
nums = list(map(int, input().split()))
plus, minus, multi = map(int, input().split())

yeonsanja = []
sum = 0
result = []
max = 0
min = 0

for _ in range(plus):
    yeonsanja.append("+")
for _ in range(minus):
    yeonsanja.append("-")
for _ in range(multi):
    yeonsanja.append("*")

test_yeonsanja = yeonsanja


sum = nums[0]
for i in range(1,len(nums)):   
    for j in test_yeonsanja:      
        if j == "+":
            sum = sum + nums[i]
            test_yeonsanja.pop(0)
            break
        elif j == "-":
            sum = sum - nums[i]
            test_yeonsanja.pop(0)
            break
        elif j == "*":
            sum = sum * nums[i]
            test_yeonsanja.pop(0)
            break
    result.append(sum)

print(sum)