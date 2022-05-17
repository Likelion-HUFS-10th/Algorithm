#0000한 번의 거래로 낼 수 있는 최대 이익을 산출하라.
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        List=[]
        for i in range(len(prices)):
            for j in range(i+1, len(prices)):
                a=prices[j]-prices[i]
                List.append(a)
        
        if max(List)<=0:
            print(0)
        else:
            print(max(List))
            
#Wrong answer