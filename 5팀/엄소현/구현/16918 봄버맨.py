import sys
input = sys.stdin.readline

r, c, n = map(int, input().split())   # r: 행, c: 열, n: 초
initial_grid = [list(input().strip()) for _ in range(r)]

def bomb(grid):
    current_grid = [['O' for _ in range(c)] for _ in range(r)]
    for i in range(r):
        for j in range(c):
            if grid[i][j] == 'O':
                current_grid[i][j] = '.'
                for dx, dy in (0, 1), (0, -1), (1, 0), (-1, 0):
                    x, y = i + dx, j + dy
                    if 0 <= x < r and 0 <= y < c:
                        current_grid[x][y] = '.'
    return current_grid

if n == 1:   # 초기 상태
    for i in range(r):
        print(''.join(initial_grid[i]))
elif n % 2 == 0:   # 짝수 초에는 전체에 폭탄
    for i in range(r):
        print('O' * c)
elif n % 4 == 3:   # 초기 상태에서 폭탄 터진 상태
    result_grid = bomb(initial_grid)
    for i in range(r):
        print(''.join(result_grid[i]))
elif n % 4 == 1:
    result_grid = bomb(initial_grid)
    result_grid = bomb(result_grid)
    for i in range(r):
        print(''.join(result_grid[i]))
