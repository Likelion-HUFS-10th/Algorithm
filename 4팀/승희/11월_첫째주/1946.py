'''
'''
import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input()) # 지원자의 수
    arr = [
        tuple(map(int,input().split()))
        for _ in range(n)
    ]

    arr.sort() #서류심사 순위대로 정렬하기

    result = 1

    score = arr[0][1] #서류심사에서 가장 높은 사람의 면접 순위

    for i in range(1,n):
        if score > arr[i][1]:
            result+=1
            score = arr[i][1]

    print(result)
