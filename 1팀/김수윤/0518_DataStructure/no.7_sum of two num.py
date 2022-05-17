#0000 덧셈하여 타겟을 만들 수 있는 배열의 두 숫자 인덱스를 리턴하라.
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
                for i in range(len(nums)):
                    for j in range(1, len(nums)+1):
                        if i==j:
                            continue
                        elif i>j:
                            continue
                        else:
                            sum=nums[i]+nums[j]
                            if sum==target:
                                return [i,j]
                            else:
                                continue