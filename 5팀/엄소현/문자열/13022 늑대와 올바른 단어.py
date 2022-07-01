import sys
input = sys.stdin.readline

word = input().strip()

now = 0   # 현재 문자 인덱스
next = 1   # w: 1, o: 2, l: 3, f: 4
cnt = 0
cnt2 = 0

while now < len(word):
  if word[now] == "w":
    if next == 1:
      while now < len(word) and word[now] == "w":
        cnt += 1
        now += 1
      next = 2
    else:
      print(0)
      exit()
  elif word[now] == "o":
    if next == 2:
      while now < len(word) and word[now] == "o":
        cnt2 += 1
        now += 1
      if cnt == cnt2:
        next = 3
        cnt2 = 0   # 초기화
      else:
        print(0)
        exit()
    else:
      print(0)
      exit()
  elif word[now] == "l":
    if next == 3:
      while now < len(word) and word[now] == "l":
        cnt2 += 1
        now += 1
      if cnt == cnt2:
        next = 4
        cnt2 = 0   # 초기화
      else:
        print(0)
        exit()
    else:
      print(0)
      exit()
  elif word[now] == "f":
    if next == 4:
      while now < len(word) and word[now] == "f":
        cnt2 += 1
        now += 1
      if cnt == cnt2:
          next = 1
          cnt, cnt2 = 0, 0   # 초기화
      else:
          print(0)
          exit()
    else:
      print(0)
      exit()
  else:
    print(0)
    exit()

if next != 1:
  print(0)
else:
  print(1)