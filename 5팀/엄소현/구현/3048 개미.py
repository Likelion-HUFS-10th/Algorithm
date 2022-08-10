import sys
input = sys.stdin.readline

n1, n2 = map(int, input().split())   # 첫 번째 그룹 개미 수, 두 번째 그ㄹ룹 개미 수
n1_ants =list(input().strip())
n2_ants = list(input().strip())
t = int(input())

for i in range(len(n1_ants)):   # 첫 번째 그룹임 표시
  n1_ants[i] = (n1_ants[i], 1)
for i in range(len(n2_ants)):   # 두 번째 그룹임 표시
  n2_ants[i] = (n2_ants[i], 2)

pre_line = n1_ants[::-1] + n2_ants
after_line = n1_ants[::-1] + n2_ants
for _ in range(t):
  for i in range(len(pre_line)-1):
    if pre_line[i][1] == 1 and pre_line[i+1][1] == 2:
      after_line[i], after_line[i+1] = after_line[i+1], after_line[i]
  pre_line = after_line[:]

for i in range(len(after_line)):
  print(after_line[i][0], end='')