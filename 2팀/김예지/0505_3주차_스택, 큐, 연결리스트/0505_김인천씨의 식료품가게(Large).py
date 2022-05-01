# 12034 김인천씨의 식료품가게 (Large)

# by oneself
import sys
input = sys.stdin.readline

T = int(input())
for k in range(T):
    N = int(input())
    food_price = list(map(int, input().split()))

    case = []
    for i in range(N):
        if food_price[i]*4/3 in food_price:
            case.append(food_price[i])
            food_idx = food_price.index(int(food_price[i]*4/3))
            food_price.pop(food_idx)
            
    case_int = [str(c) for c in case]
    print(f'Case #{k+1}: '+ " ".join(case_int))