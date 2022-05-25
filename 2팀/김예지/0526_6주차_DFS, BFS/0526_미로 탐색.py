n, m = map(int, input().split())
graph = []

for _ in range(n):
    graph.append(list(input())) # maze 완성
    
graph[0][0] = 1 # 문자열 "1"을 정수 1로 바꿔줌.  
queue = [[0, 0]]
d = [(1, 0), (-1, 0), (0, 1), (0, -1)]

while queue:
    x, y = queue[0][0], queue[0][1]
    queue.pop(0)
    for dx, dy in d:
        X, Y = x+dx, y+dy
        if (0 <= X < n) and (0 <= Y < m) and graph[X][Y] == "1":
            queue.append([X, Y])
            graph[X][Y] = graph[x][y] + 1

print(graph[n-1][m-1])