import sys
input = sys.stdin.readline

visited = [[False for _ in range(6)] for _ in range(6)]

def check(before, move):
  alp = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5}
  befor_num = alp[before[0]]
  move_num = alp[move[0]]
  if abs(move_num - befor_num) == 2 and abs(int(move[1]) - int(before[1])) == 1 and not visited[move_num][int(move[1])-1]:
    visited[move_num][int(move[1])-1] = True
  elif abs(move_num - befor_num) == 1 and abs(int(move[1]) - int(before[1])) == 2 and not visited[move_num][int(move[1])-1]:
    visited[move_num][int(move[1])-1] = True
  else:
    return False
  return True

flag = True
for i in range(36):
  move = input().strip()
  if i == 0:
    start = move
  else:
    if not check(before, move):
      flag = False
      break
  before = move
if not check(before, start):
  flag = False

if flag:
  print("Valid")
else:
  print("Invalid")