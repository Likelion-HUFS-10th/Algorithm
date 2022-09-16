import sys
input = sys.stdin.readline

n = int(input())   # 보드 크기
candy = [list(input().strip()) for _ in range(n)]

def cal_row(i, j):
  color = candy[i][j]
  cnt = 1
  change = False
  for k in range(j+1, n):
    if color == candy[i][k]:
      cnt += 1
    else:
      if not change:
        if 0 <= i + 1 < n and color == candy[i+1][k]:   # 아래쪽 교환
          change = True
          cnt += 1
        elif 0 <= i - 1 < n and color == candy[i-1][k]:   # 위쪽 교환
          change = True
          cnt += 1
        elif 0 <= k + 1 < n  and color == candy[i][k+1]:   # 오른쪽 교환
          cnt += 1
          return cnt
        else:
          return cnt
      else:
        return cnt
  return cnt 

def cal_row_back(i, j):
  color = candy[i][j]
  cnt = 1
  change = False
  for k in range(j-1, -1, -1):
    if color == candy[i][k]:
      cnt += 1
    else:
      if not change:
        if 0 <= i + 1 < n and color == candy[i+1][k]:   # 아래쪽 교환
          change = True
          cnt += 1
        elif 0 <= i - 1 < n and color == candy[i-1][k]:   # 위쪽 교환
          change = True
          cnt += 1
        elif 0 <= k - 1 < n  and color == candy[i][k-1]:   # 왼쪽 교환
          cnt += 1
          return cnt
        else:
          return cnt
      else:
        return cnt
  return cnt 

def cal_col(i, j):
  color = candy[i][j]
  cnt = 1
  change = False
  for k in range(i+1, n):
    if color == candy[k][j]:
      cnt += 1
    else:
      if not change:
        if 0 <= j + 1 < n  and color == candy[k][j+1]:   # 오른쪽 교환
          change = True
          cnt += 1
        elif 0 <= j - 1 < n  and color == candy[k][j-1]:   # 왼쪽 교환
          change = True
          cnt += 1
        elif 0 <= k + 1 < n and color == candy[k+1][j]:   # 아래쪽 교환
          cnt += 1
          return cnt
        else:
          return cnt
      else:
        return cnt
  return cnt

def cal_col_back(i, j):
  color = candy[i][j]
  cnt = 1
  change = False
  for k in range(i-1, -1, -1):
    if color == candy[k][j]:
      cnt += 1
    else:
      if not change:
        if 0 <= j + 1 < n  and color == candy[k][j+1]:   # 오른쪽 교환
          change = True
          cnt += 1
        elif 0 <= j - 1 < n  and color == candy[k][j-1]:   # 왼쪽 교환
          change = True
          cnt += 1
        elif 0 <= k - 1 < n and color == candy[k-1][j]:   # 위쪽 교환
          cnt += 1
          return cnt
        else:
          return cnt
      else:
        return cnt
  return cnt

max_cnt = 0
for i in range(n):
  for j in range(n):
    max_cnt = max(max_cnt, cal_row(i, j))
    max_cnt = max(max_cnt, cal_col(i, j))
    if max_cnt == n:
      print(max_cnt)
      exit(0)

for i in range(n-1, -1, -1):
  for j in range(n-1, -1, -1):
    max_cnt = max(max_cnt, cal_row_back(i, j))
    max_cnt = max(max_cnt, cal_col_back(i, j))
    if max_cnt == n:
      print(max_cnt)
      exit(0)

print(max_cnt)
