import collections

nums = [-1,0,1,2,-1,-4]
lists = collections.defaultdict(list)
hap = 0

for i in range(len(nums)-1):
    for k in range(1,len(nums)):
        hap = nums[i] + nums[k]
        
        if (0-hap) in nums and nums.index(0-hap) != i and nums.index(0-hap) != k:
            lists[i].append(nums[i])
            lists[i].append(nums[k])
            lists[i].append(0-hap)
    hap = 0

print(list(lists.values()))

#아직 안됨