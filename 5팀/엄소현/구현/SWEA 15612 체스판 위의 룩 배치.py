t = int(input())   # 테스트 케이스 개수

def count():
  row = [0, 0, 0, 0, 0, 0, 0, 0]
  col = [0, 0, 0, 0, 0, 0, 0, 0]
  cnt = 0
  for i in range(8):
    for j in range(8):
      if rook[i][j] == 'O':
        row[i] += 1
        col[j] += 1
        cnt += 1
        if row[i] >= 2 or col[j] >= 2:
          return False
  if cnt == 8:
    return True
  else:
    return False

for i in range(t):
  rook = [list(input().strip()) for _ in range(8)]
  if count():
    print(f'#{i+1} yes')
  else:
    print(f'#{i+1} no')
