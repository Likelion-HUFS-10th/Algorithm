import sys
from collections import deque
input = sys.stdin.readline

def solution(n, prices):
    discount = []
    while prices:
        price = prices.popleft()
        if (price // 3 * 4) in prices:
            o_price = price // 3 * 4
            discount.append(price)
            prices.remove(o_price)
    return discount

t = int(input())
for i in range(t):
    n = int(input())
    result = solution(n, deque(list(map(int, input().split()))))
    print("Case #%d:" %(i+1), *result)