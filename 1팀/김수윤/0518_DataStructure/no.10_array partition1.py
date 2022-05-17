#n개의 페어를 이용한 min(a,b)의 합으로 만들 수 있는 가장 큰 수를 출력하라.
class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        sum=0
        pair=[]
        nums.sort() #nums는 그럼.. 그냥 정수인건가?
        
        for n in nums:
            pair.append(n)
            if len(pair) == 2: #결국에 n이 3보다 커지면..if문 안걸리는거 아닌가..? 음?
                sum += min(pair)
                pair=[]
                
        return sum