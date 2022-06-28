import sys
input = sys.stdin.readline

def back():
    global cnt
    if sum(result) < 0:
        return
    if len(result) == n:
        cnt += 1
        return
    for i in range(len(a)):
        if not visited[i]:
            visited[i] = True
            result.append(a[i])
            back()
            visited[i] = False
            result.pop()


n, k = map(int, input().split())
a = list(map(int, input().split()))
a = [(i - k) for i in a]
visited = [False] * (n+1)
result = []
cnt = 0
back()
print(cnt)