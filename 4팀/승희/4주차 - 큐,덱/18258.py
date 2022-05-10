"""
계속 시간초과가 남 => deque 안써서 (pop 때문인듯) + sys.stdin.readline
"""
from collections import deque
import sys

q = deque([])
input = sys.stdin.readline
n = int(input())

order_arr = [
    tuple(input().split())
    for _ in range(n)
]

for i in range(n):
    if len(order_arr[i])==2:
        order,num = order_arr[i]
    else:
        order = order_arr[i][0]

    if order=="push":
        q.append(num)
    elif order=="pop":
        if len(q)==0:
            print(-1)
        else:
            print(q.popleft())
    elif order=="size":
        print(len(q))
    elif order=="empty":
        if len(q)==0:
            print(1)
        else:
            print(0)
    elif order=="front":
        if not q:
            print(-1)
        else: print(q[0])
    elif order=="back":
        if not q:
            print(-1)
        else: print(q[-1])
