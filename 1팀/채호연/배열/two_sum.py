# #0. 나의 해답
# def twoSum(nums: list, target: int) -> list:
#     indx = []
#     for i in nums:
#         if i < target:
#             if target - i in nums and nums.index(i) != nums.index(target - i): #i = target - i
#                     indx.append(nums.index(i))
#                     indx.append(nums.index(target - i))
                    
#                     return indx

# print(twoSum([3, 3], 6)) # 여기가 통과가 안 됩니다,,,


'''
#1. 브루트포스를 이용한 해결
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
O(n^2)
'''
'''
2. in을 이용한 탐색
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, n in enumerate(nums):
            comp = target - n
            if comp in nums[i+1:]:
                return [nums.index(n), nums[i+1:].index(comp) + (i+1)]

O(n^2) : 하지만 in 은 매번 값을 비교하는 것보다 훨씬 빠름
'''

'''
#3. 첫 번 째수를 뺀 결과를 키 값으로 조회 : 진짜 이건 생각도 못했고 너무 기똥차서 물구나무를 섰다
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_map = {}
        for i, n in enumerate(nums):
            nums_map[n] = i
            
        for i, n in enumerate(nums):
            if target - n in nums_map and i != nums_map[target - n]:
                return [i, nums_map[target - n]]
'''
'''
#4. 3의 조회구조 개선 : 2개의 for을 하나의 for로 합쳐서 처리.

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_map = {}
        for i, n in enumerate(nums):
            if target - n in nums_map:
                return [nums_map[target - n], i]
            nums_map[n] = i
'''
'''
#5. 투 포인터 이용
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        left, right = 0, len(nums) - 1
        while not left == right:
            if nums[left] + nums[right] < target:
                left += 1
            elif nums[left] + nums[right] > target:
                right -= 1
            else:
                return[left, right]

'''