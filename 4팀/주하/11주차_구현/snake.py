n = int(input())
apple = int(input())

data = [[0]*(n+1) for _ in range(n+1)]  # 맵 크기
rot = [] # 뱀 방향 회전 정보들 담기

for _ in range(apple) :
    row, col = map(int, input().split())
    data[row][col] = 1  # 사과가 있는 곳은 1로 표시

snake_info= int(input())  # 뱀 회전 정보(초, 방향)
for _ in range(snake_info):
    x, c = input().split()
    rot.append((int(x), c))

# 90도 방향 회전 (뱀 처음에 오른쪽 향함) 동 -> 남 -> 서 -> 북
dx = [0,1,0,-1]
dy = [1,0,-1,0]

def turn(now_dir, c):  # 뱀 회전에 따른 현재 방향 함수
    if c == 'L':
        now_dir = (now_dir - 1) % 4
    else: 
        now_dir = (now_dir + 1) % 4
    return now_dir

def start():
    x, y = 1,1        # 뱀 시작 위치
    data[x][y] = 2    # 뱀이 있는 곳은 2로 표시
    now_dir = 0       # 뱀이 처음에는 동쪽을 보고 출발
    time = 0          # 시작한 뒤에 지난 초
    idx = 0           # 다음 회전 방향 인덱스
    q = [(x, y)]      # 뱀이 차지하고 있는 위치 정보

    while True : 
        nx  = x + dx[now_dir]
        ny = y + dy[now_dir]
        if 1 <= nx and nx <= n and 1 <= ny and ny <= n and data[nx][ny] !=2:   # 맵 범위 안에 있고, 뱀이 이미 위치한 곳이 아니면(몸통 있는 곳)
            if data[nx][ny] == 0:    # 사과가 없다면
                data[nx][ny] = 2     # 몸통이동 + 꼬리 지우기
                q.append((nx, ny))
                px, py = q.pop(0)
                data[px][py] = 0

            if data[nx][ny] == 1:   # 사과가 있다면
                data[nx][ny] = 2    # 몸통이동 +  꼬리 그대로
                q.append((nx, ny))

            else:                   # 벽이나 몸통에 부딪힌 경우
                time += 1           # 시간 추가
                break

            x,y = nx,ny             # 다음 위치로 이동
            time += 1

            if idx < snake_info and  time == rot[idx][0]:     # 회전해야하는 시간일 경우
                now_dir = turn(now_dir, rot[idx][1])
                idx += 1
        return time

print(start())