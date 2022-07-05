"""
앞뒤 숫자가 무조건 1 차이
배열 > 뒤에는 1 크거나, 1 작거나
0과 9를 제외하고는 동일(0,9 > 1개, 나머지 > 2개)
빈리스트를 통해 dp를 계속 업데이트 시켜주는 방법 사용
"""
N = int(input())

dp = [0] + [1] * 9

for i in range(1,N):
    arr = []
    for j in range(10):
        if j == 0:
            arr.append(dp[1])
        elif j == 9:
            arr.append(dp[8])
        else:
            arr.append(dp[j-1] + dp[j+1])
    dp = arr

print(sum(dp)%1000000000)