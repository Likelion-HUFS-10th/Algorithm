from collections import deque

num = int(input())
for _ in range(num):
    cnt = 0
    n, m = map(int,input().split())
    order = deque(list(map(int,input().split())))
    target_idx = m
    while True:
        if order[0] == max(order):
            order.popleft()
            cnt += 1
            if target_idx == 0:
                break
            else:
                target_idx -=1

        else:
            remove_order = order.popleft()
            order.append(remove_order)
            if target_idx == 0:
                target_idx = len(order)-1
            else:
                target_idx -= 1
            
    print(cnt)

                    




        