'''
<큐>

+ 이것두 시간초과 

import sys
input = sys.stdin.readline

+ 출력 예시는 같은데 정답은 틀림..?

'''
import sys
input = sys.stdin.readline

n = int(input())
order_list = []
for _ in range (n):
    order = input().split()
    if order[0] == 'push':
        order_list.append(order[1])
    elif order[0] == 'pop':
        if len(order_list) == 0:
            print(-1)
        else:
            print(order_list.pop())
    elif order[0] == 'size':
        print(len(order_list))
    elif order[0] == 'empty':
        if len(order_list) == 0:
            print(1)
        else:
            print(0)
    elif order[0] == 'front':
        if len(order_list) == 0:
            print(-1)
        else:
            print(order_list[0])
    elif order[0] == 'back':
        if len(order_list) == 0:
            print(-1)
        else:
            print(order_list[-1])
