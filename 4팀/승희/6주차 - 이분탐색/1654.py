"""
너무 어려웠음!!!!! 왜이러지!!!!!!!!!!!!!!!!!!!!!!!!!!
아무런 생각이 안들었음.. ㅜ ㅜ ㅜ ㅜ ㅜ ㅜ
구글링해서 코드를 참고하고 직접 재귀로 바꿨음
"""
import sys

input = sys.stdin.readline

k,n = map(int,input().split())
arr = [int(input()) for _ in range(k)]
start,end = 1,max(arr)

def binary(start,end,n):
    if start > end:
        return end
    mid = (start+end)//2
    lines = 0
    for i in arr:
        lines += i//mid #기준이 되는 지점만큼 자르기
    if lines >= n:
        return binary(mid+1,end,n)
    elif lines < n:
        return binary(start,mid-1,n)

print(binary(start,end,n))
