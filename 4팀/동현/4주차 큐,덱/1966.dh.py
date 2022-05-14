"""
큐를 활용하는 방법으로 다시 접근
기존 방식에서는 같은 숫자 처리가 불가능..
인덱스를 활용하는 방안 참고
"""
from collections import deque

n = int(input())

for i in range(n):
    N,M = map(int, input().split())
    num_list = deque(list(map(int,input().split())))
    find_idx = M
    count = 1
    while True:
        if max(num_list) == num_list[0]:
            num_list.popleft()
            if find_idx == 0:
                print(count)
                break
            # 아래 elif문이랑 충돌
            #elif find_idx != 0 and num_list[find_idx] == max(num_list):
                #print(count + find_idx)
            else:
                find_idx -= 1
                count += 1
                
        elif max(num_list) != num_list[0]:
            pop_num = num_list.popleft()
            num_list.append(pop_num)
            if find_idx == 0:
                find_idx = len(num_list) -1
            else:
                find_idx -= 1