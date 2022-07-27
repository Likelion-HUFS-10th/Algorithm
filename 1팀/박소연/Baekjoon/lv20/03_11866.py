# 요세푸스 문제
# 큐로 풀기

from collections import deque

que, answer = deque(), []
n, k = map(int, input().split())

for i in range(n):
  que.append(i+1)

while que:
  for _ in range(k-1):
    # 원하는 인덱스 전까지의 수들은 맨뒤로 붙고
    que.append(que.popleft())
  # for문 나오면 원하는 숫자가 맨위에 있음
  # popleft()로 빼고 answer에 append
  answer.append(que.popleft())
print("<", end="")
for i in range(len(answer) - 1):
  print(str(answer[i]) + ",", end=" ")
print(str(answer[-1]), end="")
print(">")