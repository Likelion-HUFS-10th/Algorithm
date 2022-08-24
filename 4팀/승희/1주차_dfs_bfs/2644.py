from collections import deque

n = int(input()) #전체 사람의 수

p_1, p_2 = map(int,input().split()) #촌수를 계산해야 하는 두 사람의 번호

arr = [
    []
    for _ in range(n+1)
]

m = int(input()) #부모-자식 간의 관계의 개수

for _ in range(m):
    x,y = map(int,input().split())
    # children[y].append(x)
    # parents[x].append(y)
    arr[x].append(y)
    arr[y].append(x)

visited = [
    False for _ in range(n+1)
]

distance = [
    0 for _ in range(n+1)
]

def bfs(x):
    q = deque([x])
    visited[x] = True
    # Flag = False

    while q:
        now = q.popleft()
        visited[now] = True
        for n in arr[now]:
            if not visited[n]:
                distance[n] = distance[now]+1
                q.append(n)

bfs(p_1)

if distance[p_2] != 0:
    print(distance[p_2])
else:
    print(-1)

    #     if len(parents[now])==0:
    #         continue
    #     else:
    #         parent = children[now][0]
    #         if not visited[parent]:
    #             q.append(parent)

    #     for i in range(len(parents[parent])):
    #         if not visited[i]:
    #             visited[i] = True
    #             distance[i] = distance[now]+1
    #             q.append(i)

    #         if i == p_2:
    #             Flag = True
    #             print(distance[p_2])
    # if not Flag:
    #     print(-1)

# def bfs(x,y):
#     q = deque([x])
#     visited[x] = True
#     Flag = False

#     while q:
#         now = q.popleft()
#         for i in range(len(parents[now]))

# bfs(p_1, p_2)


# print("parents")
# for i in range(len(parents)):
#     print(parents[i])

# print("+++++++++++++")

# print("children")
# for i in range(len(children)):
#     print(children[i])