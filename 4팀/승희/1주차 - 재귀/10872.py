import sys
sys.setrecursionlimit(10**6)

n = int(input())

"""
계속 메모리 초과..
-> 0 입력했을 때 1이 나온다는 조건을 제대로 보지 않아서 ....
-> 원래는 if num==1 하고 0까지 가지 않도록 했음 
-> 0이 입력되면 오류가 남 (아마 더 깊이 계속해서 들어가는 듯)
"""

def cal(num):
    if num==0:
        return 1
    else:
        return cal(num-1)*num

print(cal(n))