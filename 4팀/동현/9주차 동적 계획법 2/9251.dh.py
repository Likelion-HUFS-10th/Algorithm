"""
부분수열 띄어서도 가능
순회하며 알파벳이 같을 경우 dp에 1을 더해서 저장
알파벳이 다를 경우 최댓값을 구함
"""
import sys
words = []
for _ in range(2):
    words.append(input())

n = len(words[0])
m = len(words[1])

dp = [[0] * (n+1)] * (m+1) # 이전값 사용 > 하나씩 더 크게 배열 지정

for i in range(1,n+1):
    for j in range(1,m+1):
        if words[0][i-1] == words[1][j-1]:
            dp[i][j] = dp[i-1][j-1] + 1 # 글자가 같은 경우 이전 값에 1을 더함
        else:
            dp[i][j] = max(dp[i][j-1], dp[i-1][j]) # 글자가 다른 경우 2가지 경우의 수에서 최댓값 사용

print(dp[-1][-1]) # dp의 마지막 값이 최댓값


