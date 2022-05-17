import collections

nums = [-1,0,1,2,-1,-4]

nums.sort() #nums = [-4,-1,-1,0,1,2]
lists = collections.defaultdict(list)


for i in range(len(nums)-2):
    for k in range(i+1,len(nums)-1):
        for j in range(k+1,len(nums)):
            if nums[j] + nums[i] + nums[k] == 0 :
                lists[i].append(nums[i])
                lists[i].append(nums[k])
                lists[i].append(nums[j])
        if nums[j] + nums[i] + nums[k] == 0 :
            break    
               
   

print(list(lists.values()))


