import sys

sys.setrecursionlimit(2500)
input = sys.stdin.readline

n = int(input())
arr = list(map(int,input().split())) #배열
m = int(input()) #존재하는지 알아볼 숫자들의 개수
matching_num = list(map(int,input().split()))

arr.sort()

def binary_search(num,start,end):
    i = (start+end)//2
    if start > end:
        return False
    if arr[i]==num:
        return True
    elif num > arr[i]:
        return binary_search(num,i+1,end)
    else:
        return binary_search(num,start,i-1)

for i in range(m):
    if binary_search(matching_num[i],0,n-1):
        print(1)
    else:
        print(0)

#num은 맞추려고 하는 숫자
# for i,num in enumerate(matching_num):
#     if num>arr[-1] or num<arr[0]:
#         print(0)
#     else:
#         flag=False
#         idx = (n-1)//2 #arr의 가운데
#         while idx>=0 and idx<n:
#             if num==arr[idx]:
#                 flag=True
#                 break
#             elif num > arr[idx]:
#                 idx = (idx+1+(n-1))//2
#             else:
#                 idx = (idx-1)//2
#         if flag:
#             print(1)
#         else:
#             print(0)
