import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
speed = list(map(int, input().split()))
speed = deque(speed)
rotate_cnt = 0
earth = 0

while rotate_cnt < n:
    if speed[0] < speed[1]:
        speed.rotate(-1)
        rotate_cnt += 1
    else:
        if speed[0] % speed[1] == 0:
            speed[1] = speed[0]
            speed.rotate(-1)
            rotate_cnt += 1
        else:    
            speed[1] = speed[1] * ((speed[0] // speed[1]) + 1)
            speed.rotate(-1)
            rotate_cnt += 1
            
print(speed[0])

