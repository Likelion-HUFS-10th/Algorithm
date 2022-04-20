"""
어차피 수의 범위가 적으니
수 전체에 대하여 배열을 만들고 
count를 해서 이 횟수만큼 출력을 했습니다. 
"""
import sys

max_size = 10001
n = int(input()) # 개수
arr = [0]*max_size

for _ in range(n):
    arr[int(sys.stdin.readline())] += 1

for i in range(max_size):
    if arr[i]!=0:
        for j in range(arr[i]):
            print(i)