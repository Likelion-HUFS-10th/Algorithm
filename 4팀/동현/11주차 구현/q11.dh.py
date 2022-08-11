"""
범위를 벗어나거나, 본인을 만날경우 끝
큐의 popleft 사용
사과의 유무에 따라 뱀의 길이 변화, 꼬리의 움직임
사과 O -> 꼬리 안움직임, 사과 X -> 꼬리 움직임
꼬리의 위치를 기억하기 위해 큐 사용
"""
from collections import deque

n = int(input())
k = int(input())

arr = [[0] * n for i in range(n)] # 판 만들기 
direction = {0: (0, 1), 1: (1, 0), 2: (0, -1), 3: (-1, 0)} # 뱀의 방향 변화
q = deque() # 큐 생성 -> 뱀의 몸 기억
time = deque()

for i in range(k):
    x, y = map(int, input().split())
    arr[x-1][y-1] = 1 # 사과가 있을 경우

L = int(input())
for i in range(L):
    X, C = input().split()
    time.append([int(X), C]) # 시간과 방향 변화 저장 

def move_snake():
    d = 0 # 상하좌우 이동하기 위한 키
    count = 0 # 시간 -> 결과물
    nx, ny = 0,0 # 처음 시작
    q.append((nx, ny))
    arr[nx][ny] = 4
    while True: # 범위를 벗어나거나, 몸에 부딪힐 때까지 반복
        count += 1
        nx = nx + direction[d][0] # 다음 단계
        ny = ny + direction[d][1] # 다음 단계

        if not 0 <= nx < n or not 0 <= ny < n: # 범위를 벗어날 경우
            break
        
        if arr[nx][ny] == 1: # 사과가 있을 경우
            arr[nx][ny] = 4 # 뱀의 몸이 존재, 꼬리 그대로
            q.append((nx, ny))
        
        elif arr[nx][ny] == 0: # 사과가 없을 경우
            arr[nx][ny] = 4
            q.append((nx, ny))
            delx, dely = q.popleft() # 맨 앞에 제거 -> 꼬리가 움직였기 때문
            arr[delx][dely] = 0 # 꼬리 움직임
        
        elif arr[nx][ny] == 4: # 몸에 부딪히는 경우
            break

        if len(time) and time[0][0] == count: # 방향을 바꿔야 하는 경우
            t, nd = time.popleft()
            if nd == 'L': # 왼쪽
                d = (d+3) % 4
            elif nd == 'D': # 오른쪽
                d = (d+1) % 4
    return count

print(move_snake())