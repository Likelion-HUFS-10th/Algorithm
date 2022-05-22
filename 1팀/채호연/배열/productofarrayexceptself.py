#나의 풀이 : 메모리 usage 초과;;
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = []
        for i in range(len(nums)):
            nums_popped = nums.pop(i)
            p = 1
            for j in nums:
                p *= j
                answer.append(p)
                nums.insert(i, nums_popped)
        return answer