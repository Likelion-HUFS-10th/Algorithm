#0. 나의 풀이

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        sum = []
        for i in range(len(prices)):
            for j in range(i+1, len(prices)):
                if prices[i] < prices[j]:
                    sum.append(prices[j] - prices[i])
        return max(sum)
#브루트포스 풀이. 투 포인터에 아직 능숙하지 못하다.