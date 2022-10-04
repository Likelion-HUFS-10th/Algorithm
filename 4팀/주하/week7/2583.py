# 영역 구하기
m, n, k = map(int, input().split())

# 틀
graph = [[0] * n for _ in range(m)]
point = []
for _ in range(k):
    point.append(list(map(int, input().split())))

# 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 칠하기
for draw in point:
    for x in range(draw[0],draw[2]):
        for y in range(draw[1],draw[3]):
            graph[y][x] = 1

# 분리된 영역 크기 구하기
def find_area(x, y):
    global cnt
    graph[x][y] = 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < m and 0 <= ny < n and graph[nx][ny] == 0:
            find_area(nx,ny)
            cnt += 1

# 분리된 영역 구하기
result = []
for i in range(m):
    for j in range(n):
        if graph[i][j] == 0:
            cnt = 1
            find_area(i,j)
            result.append(cnt)


print(len(result))
print(' '.join(map(str, sorted(result))))
