# 7:23
N = list(input())
front = 0
back = 0

for i in range(int(len(N)/2)):
  front += int(N[i])

for i in range(1, int(len(N)/2)+1):
  back += int(N[-i])

if front == back:
  print("LUCKY")
else:
  print("READY")
