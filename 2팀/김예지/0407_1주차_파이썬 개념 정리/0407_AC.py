import sys
from collections import deque
input = sys.stdin.readline

T = int(input())
for i in range(T):
    p = input().strip()
    n = int(input())
    arr = input().strip()
    dq = deque(arr[1:-1].split(","))
    already_error = 0
    if n == 0:
        dq = deque()

    is_odd = False
    for i in range(len(p)):
        if p[i] == "R":
            is_odd = not is_odd
        else:
            if len(dq) == 0:
                print("error")
                already_error = 1
                break
            else:
                if is_odd:
                    dq.pop()
                else:
                    dq.popleft()

    if already_error == 1:
        continue
    else:
        if not is_odd:
            print("[" + ",".join(dq) + "]")
        else:
            dq.reverse()
            print("[" + ",".join(dq) + "]")