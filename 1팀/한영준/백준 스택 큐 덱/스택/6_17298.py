orders = int(input())
nums = list(map(int, input().split()))
oks = []
count = 0

for i in range(orders-1):
    if i == orders-2 :
        oks.append(-1)
        break
    for j in range(i+1,orders):
        if nums[i] < nums[j] :
            oks.append(nums[j])
            count +=1
    if count == 0 :
        oks.append(-1)

print(oks)
