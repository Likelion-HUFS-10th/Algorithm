from collections import deque
from math import ceil
import sys
input = sys.stdin.readline

def can_go(now, dest):
  if abs(now[0] - dest[0]) + abs(now[1] - dest[1]) <= 1000:
    return True

def bfs(home, cvs_num, cvs, fesv, visited, flag):
  q = deque()
  q.append(home)
  beer = 20
  while q:
    if flag:
      beer -= ceil((abs(now[0] - q[0][0]) + abs(now[1] - q[0][1])) / 50)
      beer += 20
    now = q.popleft()
    if can_go(now, fesv):   # 도착지까지 갈 수 있는지
      return True
    for i in range(cvs_num):  # 편의점까지 갈 수 있는지
      if visited[i] and can_go(now, cvs[i]):
          q.append(cvs[i])
          visited[i] = False
          flag = True
  return False

t = int(input())   # 테스트 케이스 개수
for _ in range(t):
  cvs_num = int(input())   # 편의점 개수
  home = tuple(map(int, input().split()))  # 상근이네 집 좌표
  cvs = [tuple(map(int, input().split())) for _ in range(cvs_num)]   # 편의점 좌표
  fesv = tuple(map(int, input().split()))   # 페스티벌 좌표
  if bfs(home, cvs_num, cvs, fesv, [True for _ in range(cvs_num)], False):
    print("happy")
  else:
    print("sad")