#배열을 입력받아 output[i]가 자신을 제외한 나머지 모든 요소의 곱셈 결과가 되도록 출력하라.
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        List=[]
        for i in range(len(nums)):
            nums.pop(i)
                        
            def multiply(nums):
                ans = 1
                for n in nums:
	                if n == 0:
                        return 0
                    ans *= n
                return ans
        
            List.append(ans)
            nums.append(i)
            
            
#error.... 탭이랑 스페이스 같이 안썼는데 왜...
TabError: inconsistent use of tabs and spaces in indentation
    return 0
Line 11  (Solution.py)