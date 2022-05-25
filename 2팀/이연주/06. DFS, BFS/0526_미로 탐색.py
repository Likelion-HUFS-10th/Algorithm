def solution(n, m, miro):
    i, j = 0, 0
    stack = [(i, j)]
    while i != n - 1 or j != m - 1:
        if i < n - 1:
            if miro[i+1][j] == 1:
                miro[i+1][j] += miro[i][j]
                stack.append((i+1, j))
        if j < m - 1:
            if miro[i][j+1] == 1:
                miro[i][j+1] += miro[i][j]
                stack.append((i, j+1))
        if i > 0:  
            if miro[i-1][j] == 1:
                miro[i-1][j] += miro[i][j]
                stack.append((i-1, j))
        if j > 0:
            if miro[i][j-1] == 1:
                miro[i][j-1] += miro[i][j]
                stack.append((i, j-1))
        temp = stack.pop(0)
        i, j = temp[0], temp[1]
    return miro[n-1][m-1]

n, m = map(int, input().split(' '))
miro = []
for i in range(n):
    miro.append([])
    temp = input()
    for j in range(m):
        miro[i].append(int(temp[j]))

print(solution(n, m, miro))