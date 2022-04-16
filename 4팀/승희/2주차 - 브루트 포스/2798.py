"""
카드의 합이 21을 넘지 않는 내에서
카드의 합을 최대한 크게!
카드에는 모두 양의 정수, n장의 카드의 값을 모두
알 수 있음. -> m을 외치면 최대한 이와 가깝게 만들어야 함.

접근 방법
1. 세장 뽑아서 각각 값을 배열에 넣기 -> 어떻게 뽑지?
2. 가장 m과 가까운 숫자 찾기
"""

import sys

n,m = map(int,input().split())

cards = list(map(int,input().split()))

result_arr = []

for i in range(n-2):
    for j in range(i+1,n-1):
        for k in range(j+1,n):
            result_arr.append(cards[i]+cards[j]+cards[k])

answer = sys.maxsize
answer_diff = sys.maxsize

for result in result_arr:
    if result > m:
        continue
    elif m-result < answer_diff:
        answer = result
        answer_diff = m-result

print(answer)