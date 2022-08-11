from collections import deque

N, L, R = map(int, input().split())
graph = []
for i in range(N):
    graph.append(list(map(int, input().split())))

unit = [[0] * N for _ in range(N)] # 연합 확인
d = [(1, 0), (-1, 0), (0, 1), (0, -1)] # 방향

def bfs(x, y, graph):
    queue = deque([(x, y)])
    while queue:
        nx, ny = queue.popleft()
        for i in range(4):
            X, Y = nx+d[i][0], ny+d[i][1]
            if X > -1 and Y > -1 and X < N and Y < N: # X와 Y가 범위 안에 있고
                if L <= abs(graph[nx][ny] - graph[X][Y]) <= R: # 인구가 조건에 맞고
                    if unit[nx][ny] == 0: # 아직 unit에 포함이 안 되어 있다면
                        unit[nx][ny] = 'u' # 연합으로 바꿔준다! 그런데 여기서 연합이 여러 개인 것을 고려하지 않음...(알파벳을 바꾸는 장치가 필요)
                        unit[X][Y] = 'u'
                        queue.append((X, Y)) # 그리고 bfs가 돌아갈 수 있도록 queue에 append 해줌.

result = 0
while True:
    cnt = 0
    people = 0

    for i in range(N):
        for j in range(N):
            bfs(i, j, graph) # (0, 0)부터 그래프의 모든 원소를 돌면서 bfs 실행

    for i in range(N):
        for j in range(N):
            if unit[i][j] == 'u':
                cnt += 1 # 연합 안에 있는 국가 개수를 세어주고
                people += graph[i][j] # 사람 수도 세어주고

    if cnt != 0: # 연합이 존재한다면
        final = people // cnt # 국경을 맞대고 있는 두 국가가 공유할 인구를 final에 저장해줌.
    else: # 연합이 존재하지 않으면
        break # break

    for i in range(N):
        for j in range(N):
            if unit[i][j] == 'u': # 연합된 국가라면 
                graph[i][j] = final # 공유할 인구를 채워준다.

    unit = [[0] * N for _ in range(N)] # unit 초기화
    result += 1 # while문 하나 돌 때마다 result += 1

print(result)
