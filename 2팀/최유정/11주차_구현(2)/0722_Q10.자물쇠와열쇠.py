key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
lock = 	[[1, 1, 1], [1, 1, 0], [1, 0, 1]]


def rotated(key):
    new_key = [[0 for y in range(len(key))] for x in range(len(key))]
    for x in range(len(key)):
        for y in range(len(key)):
            new_key[x][y] = key[y][abs(x-(len(key)-1))]
    return new_key


def check(ano_lock):
    n = len(ano_lock) // 3
    for i in range(n, 2*n):
        for j in range(n, 2*n):
            if ano_lock[i][j] != 1:
                return False
    return True


def solution(key, lock):
    m, n = len(key), len(lock)
    new_lock = [[0]* (3*n) for _ in range(3*n)]
    for i in range(n):
        for j in range(n):
            new_lock[n+i][n+j] = lock[i][j]
    for _ in range(4):
        key = rotated(key)
        for x in range(1, 2*n):
            for y in range(1, 2*n):
                for i in range(m):
                    for j in range(m):
                        new_lock[i+x][j+y] += key[i][j]
                if check(new_lock):
                    return True
                else:
                    for i in range(m):
                        for j in range(m):
                            new_lock[i+x][j+y] -= key[i][j]
    return False

print(solution(key, lock))



#copy
# import copy

# def rotated(key):
#     new_key = [[0 for y in range(len(key))] for x in range(len(key))]
#     for x in range(len(key)):
#         for y in range(len(key)):
#             new_key[x][y] = key[y][abs(x-(len(key)-1))]
#     return new_key


# def check(ano_lock):
#     n = len(ano_lock) // 3
#     for i in range(n, 2*n):
#         for j in range(n, 2*n):
#             if ano_lock[i][j] != 1:
#                 return False
#     return True


# def solution(key, lock):
#     m, n = len(key), len(lock)
#     new_lock = [[0]* (3*n) for _ in range(3*n)]
#     for i in range(n):
#         for j in range(n):
#             new_lock[n+i][n+j] = lock[i][j]
#     for _ in range(4):
#         key = rotated(key)
#         for x in range(1, 2*n):
#             for y in range(1, 2*n):
#                 ano_lock = copy.deepcopy(new_lock)
#                 for i in range(m):
#                     for j in range(m):
#                         ano_lock[i+x][j+y] += key[i][j]
#                 if check(ano_lock):
#                     return True
#     return False
