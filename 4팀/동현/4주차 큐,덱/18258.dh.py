"""
선입선출
명령은 n개 입력 받음 => 명령 + 숫자 형식 고려 by split()
시간초과 발생... 10828과의 차이 = remove 사용 
remove를 대신할 방법 => deque의 popleft 사용
"""
from collections import deque

n = int(input())
order_list = [
    tuple(input().split())
    for _ in range(n)
] 

dq = deque([])

for i in order_list:
    if i[0] == 'push':
        dq.append(i[1])
    elif i[0] == 'pop':
        if len(dq) == 0:
            print(-1)
        else:
            print(dq.popleft())
    elif i[0] == 'size':
        print(len(dq))
    elif i[0] == 'empty':
        if len(dq) == 0:
            print(1)
        else:
            print(0)
    elif i[0] == 'front':
        if len(dq) == 0:
            print(-1)
        else:
            print(dq[0])
    elif i[0] == 'back':
        if len(dq) == 0:
            print(-1)
        else:
            print(dq[-1])