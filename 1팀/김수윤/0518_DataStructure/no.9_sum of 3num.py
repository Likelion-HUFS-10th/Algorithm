#0000배열을 입력받아 합으로 0을 만들 수 있는 3개의 엘리먼트를 출력하라
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        List=[]
        for i in range(len(nums)):
            for j in range(1, len(nums)):
                for k in range(2, len(nums)):
                    if i==j or i==k or j==k:
                        continue
                    elif nums[i]+nums[j]+nums[k]==0:
                        List.append([nums[i],nums[j],nums[k]])                        
        for a in range(len(List)+1):
            if set(List[a]) == set(List[a-1]):
                List.pop(a)
        return List
    
#인덱스 에러...a가 range밖을 벗어날리가..!?
IndexError: list index out of range
    if set(List[a]) == set(List[a-1]):
Line 12 in threeSum (Solution.py)
    ret = Solution().threeSum(param_1)
Line 33 in _driver (Solution.py)
    _driver()
Line 44 in <module> (Solution.py)