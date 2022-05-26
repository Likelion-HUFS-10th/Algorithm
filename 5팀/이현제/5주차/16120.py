import sys
input = sys.stdin.readline

def bomb(map, R, C):
    for i in range(R):
        for j in range(C):
            if map[i][j] == '.':
                map[i][j] = 'O'
            elif map[i][j] == 'O':
                map[i][j] = '1'
                if j > 0:
                    map[i][j - 1] = '1'
                if j < C - 1 and map[i][j + 1] != 'O':
                    map[i][j + 1] = '1'
                if i > 0:
                    map[i - 1][j] = '1'
                if i < R - 1 and map[i + 1][j] != 'O':
                    map[i + 1][j] = '1'
    for i in range(R):
        for j in range(C):
            if map[i][j] == '1':
                map[i][j] = '.'
    return map 

def allbomb(map, R, C):
    for i in range(R):
        for j in range(C):
            map[i][j] = 'O'
    return map

def printmap(map, R, C):
    for i in range(R):
        for j in range(C):
            print(map[i][j], end='')
        print()

R, C, N = map(int, input().split())

map = [
    list(input().rstrip())
    for _ in range(R)
]


if N == 1:
    printmap(map, R, C)
elif N % 2 == 0:
    map = allbomb(map, R, C)
    printmap(map, R, C)
elif N % 4 == 3:
    map = bomb(map, R, C)
    printmap(map, R, C)
elif N % 4 == 1:
    map = bomb(map, R, C)
    map = bomb(map, R, C)
    printmap(map, R, C)
